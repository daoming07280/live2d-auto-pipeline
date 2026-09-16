"""Run Marigold (no group_offload) + PSD extract after LayerDiff succeeded."""
from __future__ import annotations

import os
import os.path as osp
import sys

ROOT = r"<PIPELINE_ROOT>\see-through-portable\see-through-portable"
os.chdir(ROOT)
sys.path.insert(0, osp.join(ROOT, "inference", "scripts"))
sys.path.insert(0, osp.join(ROOT, "common"))
os.environ["HF_HOME"] = r"<PIPELINE_ROOT>\hf-cache"
os.environ["HUGGINGFACE_HUB_CACHE"] = r"<PIPELINE_ROOT>\hf-cache\hub"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

REPO_DEPTH = "24yearsold/seethroughv0.0.1_marigold"


def main() -> None:
    save_dir = r"<PIPELINE_ROOT>\jobs\test01\02_layers"
    imgp = osp.join(save_dir, "character.png")
    saved = osp.join(save_dir, "character")

    print("import torch / marigold", flush=True)
    import torch
    from utils.inference_utils import apply_marigold, further_extr
    from utils.torch_utils import seed_everything

    print("cuda", torch.cuda.is_available(), flush=True)
    seed_everything(42)

    print("[marigold] no group_offload", flush=True)
    apply_marigold(
        imgp,
        REPO_DEPTH,
        save_dir=save_dir,
        seed=42,
        resolution=-1,
        disable_progressbar=False,
        cache_tag_embeds=True,
        group_offload=False,
    )

    print("[extract] further_extr", flush=True)
    further_extr(saved, rotate=False, save_to_psd=True, tblr_split=True)

    psd = osp.join(save_dir, "character.psd")
    print("psd exists:", osp.exists(psd), psd, flush=True)
    if osp.isdir(saved):
        for n in sorted(os.listdir(saved)):
            print(" ", n, flush=True)


if __name__ == "__main__":
    main()

