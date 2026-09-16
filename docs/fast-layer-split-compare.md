---
feature: fast-layer-split-compare
status: delivered
updated: 2026-09-16
branch: (none 鈥?pipeline-root not a git worktree)
commits: n/a
---

# 蹇€熸媶灞傚弻璺緞瀵规瘮锛堥伩寮€ See-through 闀胯€楁椂锛?
## Report

**What was built** 鈥?鐢ㄦ埛鎵瑰噯鍚庡皢 [0ran/puppet-part-splitter](https://github.com/0ran/puppet-part-splitter) 閮ㄧ讲鍒?`pipeline-root\puppet-part-splitter`锛坣pm install 鎴愬姛锛孷ite `http://127.0.0.1:5173` 杩斿洖 200锛夈€傚苟琛岀敤璁惧畾鍥捐涓荤珛缁?+ 杩為€氬煙鎷嗗垎 + ag-psd 缁?PSD 鍋氳矾寰?B銆傜粨璁猴細**涓ゆ潯蹇€熻矾寰勯兘鏃犳硶浜у嚭 psd2live 鍙敤鐨勮涔夊垎灞?*锛泂plitter 鏄祻瑙堝櫒绔繛閫氬煙/PSD 灞傚伐鍏凤紝涓嶆槸 See-through 鏇夸唬鍝併€?
**Verification** 鈥?`npm install` 閫氳繃锛沄ite HTTP 200锛汸ython 澶嶇幇 splitter 绠楁硶瀵逛富绔嬬粯寰?1 涓富杩為€氬潡锛堢害 11 涓囧儚绱狅級+ 纰庣墖锛沗whale_sheet_parts.psd` 缁?`psd_precheck` **闃绘柇锛氱己 face**銆?
**Journey log**
1. GitHub 鏃犳垚鐔熴€岄潪 See-through銆嶈涔夋媶灞傞」鐩紱splitter 鏄熷皯涓斿畾浣嶄笉鍚屻€?2. 涓嶉€忔槑绔嬬粯涓婅繛閫氬煙鎷嗗垎鍑犱箮寰楀埌鏁村彧瑙掕壊锛屾媶涓嶅嚭鐪?鍢?鍙戙€?3. 璁惧畾鍥鹃儴浠舵槸鍙傝€冪缉鐣ワ紝涓嶈兘褰撶敓浜у眰锛涚粍 PSD 涔熻繃涓嶄簡棰勬銆?4. 瑕佸揩涓斿彲鐢細浠嶉渶**鐪熷垎灞傚伐绋?*锛屾垨鎺ュ彈 See-through 闄嶉厤锛?40/20锛夋崲鏃堕棿銆?5. 鐢ㄦ埛鍒ゅ畾 splitter 涓嶅彲鐢紱宸插垹闄?`pipeline-root\puppet-part-splitter` 鍙婄浉鍏?zip/鑴氭湰娈嬬暀銆?
---

## [S1] Problem

See-through 杩囨參锛涢渶鎺㈢储鏇村揩鎷嗗眰骞朵笌銆岃鍥?鐜版湁宸ュ叿銆嶅姣斻€?
## [S2] Design

### 閮ㄧ讲锛堝凡鎵瑰噯锛涘悗缁忕敤鎴疯姹傚垹闄わ級

- ~~璺緞锛歚pipeline-root\puppet-part-splitter`~~ **宸插垹闄わ紙2026-09-16锛?*
- 渚濊禆锛歚npm install`锛坅g-psd銆乯szip銆乿ite锛?- 鍚姩锛歚npm run dev` 鎴?`start.cmd` 鈫?`http://127.0.0.1:5173`
- 璁稿彲锛氫粨搴撴棤 LICENSE 鏂囦欢锛堢鏈?鏈０鏄庯級锛涗粎鏈満璇曢獙

### 璺緞 A 鈥?puppet-part-splitter

娴忚鍣ㄥ伐鍏凤細閫忔槑鑳屾櫙杩為€氬煙鎷嗗垎 / 宸叉湁 PSD 鎶藉眰 / 鍥鹃泦鎵撳寘銆? 
**涓嶅仛**浜屾鍏冭涔夐儴浠讹紙face/eyewhite/mouth锛夊垎瑙ｃ€?
瀹炴祴锛堜笌 README 绠楁硶涓€鑷寸殑 Python 澶嶇幇锛岃緭鍏ヨ鍒囦富绔嬬粯 450脳670锛夛細

| 鎸囨爣 | 缁撴灉 |
|------|------|
| 鑰楁椂 | 绉掔骇 |
| 鈮?0px 杩為€氬潡 | 24 涓?|
| 鏈€澶у潡 | 绾?111770 px 鈮?**鏁村彧瑙掕壊** |
| 鍏朵綑 | 鏂囨湰/椋樺甫/纰庣墖 |
| Live2D 璇箟灞?| **鏃?* |

### 璺緞 B 鈥?璁惧畾鍥捐鍒?+ 鐜版湁宸ュ叿

| 姝ラ | 缁撴灉 |
|------|------|
| 瑁佷富绔嬬粯 | `jobs/whale_sheet/01_crop/main_character.png`锛?50脳670锛?|
| 杩為€氬煙鎷?| `jobs/whale_sheet/splitter_like/` |
| ag-psd 缁?PSD | `jobs/whale_sheet/03_psd/whale_sheet_parts.psd`锛? 灞傦級 |
| psd_precheck | **闃绘柇锛氱己灏?face**锛涚己 eyewhite/mouth/hair 绛?|

### 瀵规瘮缁撹

| 缁村害 | A splitter | B 瑁佸浘+缁勮 | See-through锛堝鐓э級 |
|------|------------|-------------|---------------------|
| 鑰楁椂 | 绉掞綖鍒嗛挓 | 鍒嗛挓 | 0.5锝炴暟灏忔椂 |
| 璇箟灞?| 鍚?| 鍚?| 鏄?|
| 杩?psd_precheck | 鍚?| 鍚?| 閫氬父鍙繃锛堝槾寮犲紑鏃讹級 |
| 鎺?psd2live | 鍚?| 鍚?| 鏄?|
| 閫傜敤 | 宸查€忔槑鎷嗕欢銆丳SD 鎶藉眰 | 蹇€熼瑙堟嫾璐?| 鐢熶骇缁戦婧?|

**鐢ㄦ埛鐩爣銆屽揩涓旇兘鍑?Live2D銆嶅湪鏃犵湡鍒嗗眰婧愭椂鏃犳硶鍚屾椂婊¤冻銆?*

## [S3] Out of Scope

- 涓嶉噸璺?See-through  
- 涓嶆敼 VTS test01/test02  
- 涓嶇户缁儴缃?LayerDiffuse 绛夊叾瀹冮」鐩? 

---

## Tasks

- [x] T1: clone splitter 骞跺鏌?README 鈥?acceptance: 灏变綅銆佸畾浣嶆槑纭?(covers: S2)
- [x] T2: 瀹夎渚濊禆骞堕獙璇?鈥?acceptance: npm OK + Vite 200 (covers: S2)
- [x] T3: 璺緞 B 瑁佸浘骞剁粍 PSD 鈥?acceptance: PSD 浜у嚭 + 棰勬缁撴灉 (covers: S2)
- [x] T4: 瀵规瘮骞跺啓缁撹 鈥?acceptance: 鏈姤鍛?(covers: S2)

