"""Fix test03: drop cheek ear, rebuild mouth from source pixels (with lips)."""
from __future__ import annotations

import json
import os
import os.path as osp
import sys

import numpy as np
from PIL import Image, ImageFilter
from psd_tools import PSDImage

ORDER_BOTTOM_TO_TOP = [
    "back hair",
    "back hair-l",
    "back hair-r",
    "tail",
    "wings",
    "legwear",
    "footwear",
    "bottomwear",
    "topwear",
    "handwear",
    "handwear-l",
    "handwear-r",
    "neck",
    "neckwear",
    "face",
    "ears",
    "ears-l",
    "ears-r",
    "earwear",
    "nose",
    "eyewhite",
    "eyewhite-l",
    "eyewhite-r",
    "irides",
    "irides-l",
    "irides-r",
    "eyebrow",
    "eyebrow-l",
    "eyebrow-r",
    "eyelash",
    "eyelash-l",
    "eyelash-r",
    "facedetail",
    "facedetail-l",
    "facedetail-r",
    "mouth",
    "front hair",
    "front hair-l",
    "front hair-r",
    "headwear",
    "headwear-l",
    "headwear-r",
    "eyewear",
    "objects",
]


def sort_key(name: str) -> int:
    name = name.strip()
    if name in ORDER_BOTTOM_TO_TOP:
        return ORDER_BOTTOM_TO_TOP.index(name)
    for i, tag in enumerate(ORDER_BOTTOM_TO_TOP):
        if name.startswith(tag):
            return i
    return 999


def main() -> None:
    src_psd = sys.argv[1]
    src_img = sys.argv[2]  # 768 padded source
    out_raw = sys.argv[3]
    os.makedirs(out_raw, exist_ok=True)

    psd = PSDImage.open(src_psd)
    src = Image.open(src_img).convert("RGBA")
    if src.size != (psd.width, psd.height):
        src = src.resize((psd.width, psd.height), Image.LANCZOS)
    src_arr = np.array(src)

    # mouth region with lip margin
    mx0, my0, mx1, my1 = 365, 266, 407, 313
    pad = 18
    mx0, my0 = max(0, mx0 - pad), max(0, my0 - pad)
    mx1, my1 = min(psd.width, mx1 + pad), min(psd.height, my1 + pad)

    layers_out = []  # top-to-bottom names for meta; we'll reverse for write
    skip = {"ears-r"}  # cheek false-positive ear
    # ears-l: keep if it extends past face right edge (side ear)

    face = [l for l in psd if l.name == "face"][0].composite().convert("RGBA")
    face_bb = Image.fromarray(np.array(face)[..., 3]).getbbox()
    face_right = face_bb[2] if face_bb else 483

    drop = set(skip)
    for l in psd:
        if l.name == "ears-l":
            img = l.composite().convert("RGBA")
            bb = Image.fromarray(np.array(img)[..., 3]).getbbox()
            if bb and bb[2] <= face_right + 2:
                drop.add("ears-l")

    for layer in psd:
        name = layer.name
        if name in drop:
            print("drop", name)
            continue
        img = layer.composite()
        if img is None:
            continue
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        arr = np.array(img)

        if name == "mouth":
            # rebuild from source pixels in mouth ROI, keep original mouth alpha as mask
            new = np.zeros_like(arr)
            roi_src = src_arr[my0:my1, mx0:mx1].copy()
            old_a = arr[my0:my1, mx0:mx1, 3].astype(np.float32)
            # dilate mask a bit for lips
            mask = Image.fromarray((old_a > 20).astype(np.uint8) * 255)
            mask = mask.filter(ImageFilter.MaxFilter(9))
            mask = mask.filter(ImageFilter.GaussianBlur(2))
            m = np.array(mask).astype(np.float32) / 255.0
            # also include a soft disk around mouth center for lips from source
            cy, cx = (my0 + my1) // 2, (mx0 + mx1) // 2
            yy, xx = np.mgrid[my0:my1, mx0:mx1]
            disk = ((xx - cx) ** 2 + (yy - cy) ** 2) <= (max(mx1 - mx0, my1 - my0) / 2 + 4) ** 2
            alpha = np.clip(np.maximum(m, disk.astype(np.float32) * 0.85), 0, 1)
            # source may have white bg; use original mouth alpha as primary, source RGB
            new[my0:my1, mx0:mx1, :3] = roi_src[..., :3]
            new[my0:my1, mx0:mx1, 3] = (alpha * 255).astype(np.uint8)
            arr = new
            print("mouth rebuilt from source ROI", (mx0, my0, mx1, my1))

        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in name)
        path = osp.join(out_raw, f"{safe}.raw")
        arr.tofile(path)
        layers_out.append({"name": name, "w": psd.width, "h": psd.height, "raw": f"{safe}.raw"})

    # layers_out is top-to-bottom from psd_tools; sort bottom-to-top for draw
    layers_out.sort(key=lambda x: sort_key(x["name"]))
    # reverse so first written is bottom (ag-psd children[0] = bottom in our previous working fwd draw)
    # v2_draw_fwd used list order first=back hair and looked correct when drawing first-to-last
    # meta for node: children = order as draw sequence bottom->top = layers_out
    meta = {"w": psd.width, "h": psd.height, "layers": layers_out}
    json.dump(meta, open(osp.join(out_raw, "meta.json"), "w"))
    print("kept", len(layers_out), "layers")
    print("draw order bottom->top:")
    for x in layers_out:
        print(" ", x["name"])


if __name__ == "__main__":
    main()

