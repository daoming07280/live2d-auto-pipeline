"""Reorder Live2D PSD layers: correct draw order + irides above eyewhite."""
from __future__ import annotations

import os
import os.path as osp
import sys

import numpy as np
from PIL import Image
from psd_tools import PSDImage

# Bottom -> top draw order for Live2D / psd2live
ORDER = [
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
    "mouth_open",
    "mouth_close",
    "front hair",
    "front hair-l",
    "front hair-r",
    "headwear",
    "headwear-l",
    "headwear-r",
    "eyewear",
    "objects",
]


def main() -> None:
    src = sys.argv[1]
    dst = sys.argv[2]
    psd = PSDImage.open(src)
    layers = list(psd)

    def sort_key(layer):
        name = layer.name.strip()
        if name in ORDER:
            return ORDER.index(name)
        # prefix match
        for i, tag in enumerate(ORDER):
            if name.startswith(tag):
                return i
        return 999

    # psd_tools iterates top->bottom; we want bottom first in file = last in top-to-bottom list
    ordered_top_to_bottom = sorted(layers, key=sort_key, reverse=True)

    # Build new PSD via raw RGBA + ag-psd in node for Cubism compatibility
    raw_dir = osp.join(osp.dirname(dst), "reorder_raw")
    os.makedirs(raw_dir, exist_ok=True)
    meta_layers = []
    for layer in ordered_top_to_bottom:
        img = layer.composite()
        if img is None:
            continue
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        full = Image.new("RGBA", (psd.width, psd.height), (0, 0, 0, 0))
        # layer.composite() is already full canvas in psd_tools
        if img.size != (psd.width, psd.height):
            full.paste(img, (layer.left, layer.top))
            arr = np.array(full)
        else:
            arr = np.array(img)
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in layer.name)
        raw_path = osp.join(raw_dir, f"{safe}.raw")
        arr.tofile(raw_path)
        meta_layers.append(
            {
                "name": layer.name,
                "w": psd.width,
                "h": psd.height,
                "raw": f"{safe}.raw",
            }
        )

    import json

    meta = {"w": psd.width, "h": psd.height, "layers": meta_layers}
    json.dump(meta, open(osp.join(raw_dir, "meta.json"), "w"))
    print("layers", len(meta_layers))
    print("order top->bottom:")
    for layer in ordered_top_to_bottom:
        print(" ", layer.name)
    print("raw_dir", raw_dir)
    print("dst", dst)


if __name__ == "__main__":
    main()

