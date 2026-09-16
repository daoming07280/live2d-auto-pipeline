"""Headless See-through decompose for jpg-to-live2d pipeline."""
from __future__ import annotations

import argparse
import os
import os.path as osp
import shutil
import sys
from datetime import datetime

ROOT = r"<PIPELINE_ROOT>\see-through-portable\see-through-portable"
os.chdir(ROOT)
sys.path.insert(0, osp.join(ROOT, "inference", "scripts"))
sys.path.insert(0, osp.join(ROOT, "common"))

# Use the already-downloaded HF cache on D:
os.environ["HF_HOME"] = r"<PIPELINE_ROOT>\hf-cache"
os.environ["HUGGINGFACE_HUB_CACHE"] = r"<PIPELINE_ROOT>\hf-cache\hub"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "8"
os.environ["MKL_NUM_THREADS"] = "8"
os.environ["OMP_NUM_THREADS"] = "8"

REPO_LAYERDIFF = "layerdifforg/seethroughv0.0.2_layerdiff3d"
REPO_DEPTH = "24yearsold/seethroughv0.0.1_marigold"


def main() -> None:
    p = argparse.ArgumentParser(description="See-through headless decompose")
    p.add_argument("--input", required=True)
    p.add_argument("--out", required=True, help="Output directory for layers/psd")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--resolution", type=int, default=768)
    p.add_argument("--steps", type=int, default=30)
    p.add_argument("--tblr", action="store_true", help="Left/right split")
    p.add_argument("--group-offload", action="store_true")
    p.add_argument("--depth-resolution", type=int, default=-1)
    args = p.parse_args()

    print("Loading torch...", flush=True)
    import torch
    print(f"  CUDA: {torch.cuda.is_available()} {torch.cuda.get_device_name(0) if torch.cuda.is_available() else ''}", flush=True)

    print("Loading inference modules...", flush=True)
    from utils.inference_utils import apply_layerdiff, apply_marigold, further_extr
    from utils.torch_utils import seed_everything

    save_dir = args.out
    os.makedirs(save_dir, exist_ok=True)

    src = osp.abspath(args.input)
    base = osp.splitext(osp.basename(src))[0]
    tmp_path = osp.join(save_dir, base + ".png")
    shutil.copy2(src, tmp_path)

    seed_everything(args.seed)
    depth_res = args.depth_resolution

    print(f"[1/3] LayerDiff res={args.resolution} steps={args.steps} ...", flush=True)
    apply_layerdiff(
        tmp_path,
        REPO_LAYERDIFF,
        save_dir=save_dir,
        seed=args.seed,
        resolution=args.resolution,
        num_inference_steps=args.steps,
        disable_progressbar=False,
        cache_tag_embeds=True,
        group_offload=args.group_offload,
    )

    print(f"[2/3] Marigold depth res={depth_res} ...", flush=True)
    apply_marigold(
        tmp_path,
        REPO_DEPTH,
        save_dir=save_dir,
        seed=args.seed,
        resolution=depth_res,
        disable_progressbar=False,
        cache_tag_embeds=True,
        group_offload=args.group_offload,
    )

    saved = osp.join(save_dir, base)
    print(f"[3/3] Extract + PSD tblr_split={args.tblr} ...", flush=True)
    further_extr(saved, rotate=False, save_to_psd=True, tblr_split=args.tblr)

    psd = osp.join(save_dir, f"{base}.psd")
    print("DONE", flush=True)
    print("psd:", psd if osp.exists(psd) else "(missing)", flush=True)
    print("layers:", saved, flush=True)
    if osp.isdir(saved):
        for name in sorted(os.listdir(saved)):
            print(" ", name, flush=True)
    if osp.exists(tmp_path):
        os.unlink(tmp_path)


if __name__ == "__main__":
    main()

