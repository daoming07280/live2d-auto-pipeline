# 推荐方案：时间与质量平衡

## 一句话

**合格原画 + See-through 768/30 + psd2live 48/4096。不要在 8GB 卡上强上 1280。**

## 硬件

- GPU: RTX 4060 Laptop ~8GB
- RAM: ~16GB
- Windows + Python 3.11 + torch 2.6.0+cu124

## 流水线

1. 原画：单人竖版、背景干净、身体正立；**嘴为最大张口**；优先半身/上半身
2. See-through：`resolution=768` `steps=30` `tblr=ON` `group_offload=ON`
3. Marigold：单独跑，`group_offload=OFF`
4. `HF_HUB_OFFLINE=1`
5. 侧别改名 → 预检 → 拆睫毛
6. 层序重排；必要时删误检层、用原图重采嘴部
7. psd2live：`--mesh-spacing 48 --atlas 4096`
8. vts_check → 导入 VTube Studio

## 耗时

半身图 768/30：LayerDiff 约 30–40 分钟；Marigold 约 1 分钟。

## 不要做

- 设定图拼版直接当层
- 连通域拆分当语义层
- 无张嘴原画却指望 moc3 自然张嘴
- 本机 1280 全身小脸日常批量

## 质量预期

| 部位 | 预期 |
|------|------|
| 转头 / idle / 发物理 | 可用 |
| 眨眼 | 大概率可用，依赖眼白/睫毛质量 |
| 张嘴 / 口型 | 必须原画张嘴 |
| 自然闭嘴 | 自动压缩不自然，需手动差分或精修 |
| 商稿 | 需 Cubism 手调 .cmo3 |
