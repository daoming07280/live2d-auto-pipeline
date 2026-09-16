# Live2D 鑷姩娴佹按绾垮疄璺佃褰?
浠?**鍗曞紶浜屾鍏冪珛缁?* 鍒?**Live2D moc3** 鐨勬湰鏈烘祦姘寸嚎瀹為獙锛歋ee-through 璇箟鎷嗗眰 鈫?PSD 棰勬/灞傚簭淇 鈫?psd2live 鑷姩缁戦銆?
> 鏈粨搴撲负**宸ヤ綔娴佷笌缁撴灉褰掓。**锛屼笉鍚ā鍨嬫潈閲嶃€佸瘑閽ヤ笌涓汉鏈満璺緞銆?
---

## 纭欢涓庤蒋浠堕厤缃紙鏈満瀹炴祴锛?
| 椤?| 閰嶇疆 |
|----|------|
| GPU | NVIDIA GeForce **RTX 4060 Laptop**锛堢害 8GB VRAM锛?|
| 鍐呭瓨 | 绾?16GB |
| 绯荤粺 | Windows |
| 鎺ㄧ悊 | Python 3.11 + PyTorch 2.6.0+cu124 |
| 鎷嗗眰 | [See-through](https://github.com/shitagaki-lab/see-through)锛圠ayerDiff + Marigold锛?|
| 缁勮 | [psd2live](https://github.com/tsunehimatoi/psd2live) v0.7.1 |
| 杈呭姪 | jpg-to-live2d-workflow 宸ュ叿锛堟敼鍚?棰勬/鎷嗙潾姣涳級 |

**鎺ㄨ崘妗ｄ綅锛堟椂闂翠笌璐ㄩ噺骞宠　锛?*锛?
```text
See-through: resolution=768  steps=30  tblr=ON  group_offload=ON
Marigold:    鍗曠嫭杩涚▼锛実roup_offload=OFF
HF_HUB_OFFLINE=1
psd2live:    --mesh-spacing 48 --atlas 4096
```

768/30 鍦ㄦ湰鏈?**LayerDiff 绾?30鈥?0 鍒嗛挓/寮?*锛堝崐韬浘瀹炴祴绾?32 鍒嗛挓锛夈€?280/30 鍙揪鏁板皬鏃讹紝8GB 鍗′笉鎺ㄨ崘鏃ュ父浣跨敤銆?
鍏抽敭琛ヤ竵锛歎Net 鍔犺浇闇€ `low_cpu_mem_usage=True`锛屽惁鍒?16GB 鍐呭瓨涓嬫槗 ACCESS_VIOLATION銆?
---

## 绀轰緥缁撴灉锛?68/30锛?
杈撳叆锛氬崐韬€?*寮犲槾**銆佽儗鏅緝骞插噣鐨勭珛缁橈紙`examples/source_open_mouth.png`锛夈€?
| 鐘舵€?| 鏂囦欢 |
|------|------|
| 寮犲槾锛堣繍琛屾椂/婧愬浘鐘舵€侊級 | `examples/result_open_mouth.png` |
| 闂槾锛堝弬鏁板帇鍚堝悗鐨勮鎰燂級 | `examples/result_closed_mouth.png` |
| 鑴搁儴棰勮 | `results/test03_v3_face_preview.png` |
| 鍙姞杞芥ā鍨嬪寘 | `results/test03_768_v3/`锛坢oc3 + model3 + physics + idle/blink + 璐村浘锛?|

### 缁撹鎽樿

1. **鐪?鍢淬€屽樊鍒嗐€嶆槸鑷姩閾捐矾鐨勪富瑕佺煭鏉?*  
   - 闂溂渚濊禆鐫瘺 U 褰?+ 鐪肩櫧鏀剁缉锛屽垎灞傝川閲忓樊鏃朵細銆屽彂鐧界┖鐪笺€嶃€? 
   - 鍢寸敤**鏈€澶у紶鍙ｅ浘鍚戜腑绾垮帇缂?*妯℃嫙闂彛锛屾病鏈夌嫭绔嬮棴鍙ｅ樊鍒嗘椂瑙傛劅鍙戞€€? 
   - 澶嶆潅鍢村瀷/鑷劧闂彛闇€瑕?*鎵嬪姩宸垎**锛坄mouth_close` 绛夛級鎴?Cubism 绮句慨銆?
2. **See-through 鎷嗗眰閰嶇疆楂樸€佽€楁椂闀?*  
   - 闇€瑕?NVIDIA CUDA 涓庢暟 GB 鏉冮噸銆? 
   - 8GB 鍗′笂 768/30 + group_offload 鎵嶆槸瀹炵敤鐐癸紱1280 杩囨參銆? 
   - 鏃犳垚鐔熴€岄潪 See-through銆嶈涔夋媶灞傛浛浠ｏ紙杩為€氬煙/璁惧畾鍥捐鍒囧潎涓嶅彲鐢級銆?
3. **灞傚簭涓庤妫€蹇呴』鍚庡鐞?*  
   - PSD 涓?`eyewhite`/`irides` 椤哄簭閿欒浼氬鑷村崟鐪煎叏鐧姐€? 
   - 鍙兘鎶婅€虫湹鐢诲埌鑴搁涓婏紙`ears-r` 璇锛夈€? 
   - 瑙?`docs/test03-eye-mouth-diagnosis.md` 涓?`scripts/fix_test03_ears_mouth.py`銆?
4. **鍘熺敾鍐冲畾涓婇檺**  
   - 鍢村繀椤诲紶寮€锛涘崐韬?涓婂崐韬紭浜庡叏韬皬鑴革紱韬綋姝ｇ珛銆佽儗鏅共鍑€銆?
---

## 鎺ㄨ崘娴佹按绾?
```text
鍚堟牸鍘熺敾
  鈫?See-through 768/30 + group_offload锛圡arigold 鍗曠嫭璺戯級
  鈫?渚у埆鏀瑰悕 / 棰勬 / 鎷嗙潾姣?  鈫?灞傚簭閲嶆帓锛坋yewhite 鍦?irides 涔嬩笅锛宐ack hair 鍦ㄥ簳灞傦級
  鈫?浜哄伐/鑴氭湰淇璇灞傘€佽ˉ鍢撮儴鍍忕礌
  鈫?psd2live mesh48 / atlas4096
  鈫?vts_check 鈫?瀵煎叆 VTube Studio
```

璇﹁ `docs/recommended-live2d-pipeline.md`銆?
---

## 鑴氭湰璇存槑

| 鑴氭湰 | 鐢ㄩ€?|
|------|------|
| `scripts/run_decompose.py` | See-through 鏃犵晫闈㈡媶灞傦紙闇€鏈満鏉冮噸涓?HF 缂撳瓨锛?|
| `scripts/finish_decompose.py` | Marigold 娣卞害 + 缁?PSD |
| `scripts/reorder_live2d_psd.py` | 鎸?Live2D 缁樺埗搴忛噸鎺掑眰 |
| `scripts/fix_test03_ears_mouth.py` | 鍘绘帀鑴搁璇鑰虫湹銆佺敤鍘熷浘閲嶉噰鍢撮儴 |
| `scripts/write_psd_v3.cjs` | 鐢?ag-psd 鍐欏嚭 Cubism 鍙 PSD |

璺緞璇锋寜鏈満鐜淇敼锛?*涓嶈**鎶婂惈 token 鐨?`config.json` 鎻愪氦鍒板叕寮€浠撳簱銆?
---

## 璁稿彲涓庣涓夋柟

- 鏈粨搴撴枃妗ｄ笌鑴氭湰锛歁IT锛堣 LICENSE锛? 
- See-through锛欰pache-2.0  
- psd2live锛欸PL-3.0  
- Live2D / Cubism / moc3 鍟嗘爣褰?Live2D Inc.  

鐢熸垚妯″瀷鐨勫晢鐢ㄤ笌骞冲彴瑙勫垯锛堝 nizima 瀵?AI 绔嬬粯鐨勯檺鍒讹級闇€鑷纭銆?
