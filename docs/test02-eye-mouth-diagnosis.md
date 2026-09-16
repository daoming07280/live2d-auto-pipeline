---
feature: test02-eye-mouth-diagnosis
status: delivered
updated: 2026-09-16
branch: (none 鈥?pipeline-root is not a git worktree)
commits: n/a
---

# test02 鐪?鍢村紓甯歌瘖鏂姤鍛?
## Report

**What was built** 鈥?瀵?VTS 涓?`test02_1280` 妯″瀷銆岀湪鐪间笉鍍忛棴鐪?/ 鍗曠溂鍙戠櫧 / 鍢村畬鍏ㄥ紶涓嶅紑銆嶇殑鏍瑰洜鎺掓煡銆傜粨璁猴細**PSD/鍘熺敾绱犳潗闂鏄富鍥狅紱blink 鍙傛暟缁戝畾鏈韩瀛樺湪涓旀甯搞€?* 鐢ㄦ埛閫夋嫨浠呭嚭鎶ュ憡銆佷笉淇銆?
**Verification** 鈥?鐩存帴璇诲彇 `character_lash.psd` 鍥惧眰 composite + alpha 缁熻锛涜鍙?`character_lash.blink.motion3.json` 涓?`character_lash.psd2live.json`锛涘鐓?VTS 鎴浘銆傚懡浠ょ粨鏋滆涓嬫枃銆岃瘉鎹€嶃€?
**Journey log**
1. 棰勬鍦ㄥ鍑哄墠宸茶鍛?mouth 楂樺姣?0.25銆侀珮搴︿粎鍗犻潰閮?1.8%锛堥槇鍊?0.35 / 5%锛夛紝褰撴椂鏈樆鏂€?2. See-through 瀵瑰叏韬浘鐨勯潰閮ㄦ媶灞傚湪 1280 鐢诲竷涓婁粛鍙湁绾?156脳168锛屼簲瀹樺儚绱犳瀬灏戜笖褰㈡€佸姡鍖栥€?3. 鐫瘺涓嬬紭鑷姩鎷嗗埌 facedetail 鍚庯紝闂溂浠嶄緷璧栧姡璐?eyewhite/eyelash锛屾棤娉曞舰鎴愯嚜鐒?U 褰㈤棴鐪笺€?4. 鏈満涓嶆槸 git 浠撳簱锛屾湭寤?worktree锛涙姤鍛婅惤鍦ㄦ祦姘寸嚎鐩綍鍐呫€?
---

## [S1] Problem

鐢ㄦ埛鍦?VTube Studio 鍔犺浇锛?
`D:\steam\steamapps\common\VTube Studio\VTube Studio_Data\StreamingAssets\Live2DModels\test02_1280`

瑙傚療鍒帮細

1. 鍙岀溂寮€鍚堜笉绗﹀悎鐪熷疄闂溂锛堟埅鍥句腑涓€鐪煎憟绌哄績鍙戠櫧锛夈€?2. 鍢村反瀹屽叏涓嶅紶寮€銆?3. 闇€瑕佸垽鏂細PSD 鍒嗗眰闂銆佸姩鐢婚棶棰橈紝杩樻槸涓よ€呴兘鏈夈€?
## [S2] Design锛堣瘖鏂粨璁猴級

### 鎬诲垽

| 闂 | 鍒ゅ畾 | 璇存槑 |
|------|------|------|
| 鍢村紶涓嶅紑 | **PSD/鍘熺敾** | mouth 鍥惧眰瀹炶川鏄棴鍙ｇ粏绾匡紝涓嶆槸鏈€澶у紶鍙ｅ浘 |
| 鐪ㄧ溂寮傚父 / 鍗曠溂鍙戠櫧 | **PSD 鍒嗗眰璐ㄩ噺** | eyewhite / irides / eyelash 褰㈡€佷笌鍍忕礌閲忎笉瓒筹紝blink 褰㈠彉鍚庤〃鐜颁负鈥滅┖鐪尖€?|
| 鍔ㄧ敾鍙傛暟 | **姝ｅ父** | `ParamEyeLOpen` / `ParamEyeROpen` 鏇茬嚎宸插啓鍏?blink motion |

**缁撹锛氫袱鑰呴兘娑夊強锛屼絾鍔ㄧ敾涓嶆槸涓诲洜锛涘厛鍧忓湪绱犳潗鍒嗗眰锛屽啀鍦ㄥ姩鐢讳笂鏀惧ぇ銆?*

### 璇佹嵁 A 鈥?mouth锛堝喅瀹氭€э級

瀵?`jobs/test02/03_psd/character_lash.psd`锛堜笌 VTS 鍐?`source_psd.psd` 鍚屾簮锛夛細

| 鍥惧眰 | 灏哄 | 涓嶉€忔槑鍍忕礌 | 鐩 |
|------|------|------------|------|
| mouth | **12脳3** | **28** | 鍑犱箮涓嶅彲瑙佺殑娣＄矇缁嗙嚎 |

棰勬鍘熸枃锛?
- mouth 楂樺姣斾粎 0.25锛堥槇鍊?0.35锛夛細鐤戜技闂彛  
- mouth 楂樺害鍙崰闈㈤儴楂樺害鐨?1.8%锛堥槇鍊?5%锛?
psd2live 瑕佹眰 **鏈€澶у紶鍙ｅ師鍥?*锛涢棴鍙ｅ浘鏃犳硶鐢熸垚鑷劧 `ParamMouthOpenY` 寮犲槾銆?
### 璇佹嵁 B 鈥?鐪肩潧閮ㄤ欢

| 鍥惧眰 | 灏哄 | 涓嶉€忔槑鍗犳瘮 | 闂 |
|------|------|------------|------|
| eyewhite-l | 37脳23 | 伪>10 绾?73%锛屛?200 绾?62% | 杩戜技瀹炲績娣＄矇鍧楋紝涓嶆槸甯︾灣瀛斿尯鍩熺殑娓呮櫚鐪肩櫧 |
| eyewhite-r | 34脳22 | 绫讳技 | 鍚屼笂 |
| irides-l/r | 23鈥?4脳21鈥?2 | 鍦嗗舰闈掔豢鍧?| 鏈夐鑹蹭絾涓庣溂鐧藉鍚堝樊 |
| eyelash-l/r | 57鈥?8脳37锛堟湁鏁?伪 妗嗙害楂?22鈥?3锛?| 伪>10 浠呯害 31% | 绯婃垚娣辫壊鍧楋紝涓嶆槸骞插噣涓婄潾姣?|
| face | 157脳168 | 鈥?| 鍏ㄨ韩 1280 鐢诲竷涓嬭劯閮ㄦ湁鏁堝尯寰堝皬 |

`psd2live.json` 瀵圭溂鐧?鐬冲瓟/鐫瘺/鐪夋瘺绛夊ぇ閲?ArtMesh 鎶ュ憡 **榛樿濮挎€佷笌 PSD 杈圭晫鍋忓樊**锛岃鏄庤嚜鍔ㄧ粦楠ㄥ湪杩欎簺灏忓浘鍏冧笂璇樊澶с€?
### 璇佹嵁 C 鈥?鍔ㄧ敾渚?
`character_lash.blink.motion3.json` 鍚細

- `ParamEyeLOpen`锛堣嚜 1.0 璧风殑鏇茬嚎锛? 
- `ParamEyeROpen`锛堣嚜 1.0 璧风殑鏇茬嚎锛?
鍙傛暟瀛樺湪锛?*涓嶆槸鈥滄病鍋氱湪鐪煎姩鐢烩€?*銆? 
闂溂鏁堟灉渚濊禆锛氱潾姣?U 褰㈠集鏇?+ 鐪肩櫧鏀剁缉 + 鐬冲瓟閬僵銆傚綋鍓嶇溂鐧借繃瀹炪€佺潾姣涘舰鎬佸樊 鈫?闂溂鏃舵洿鍍忊€滄寲绌?鍙戠櫧鈥濓紝涓庢埅鍥句竴鑷淬€?
### 璇佹嵁 D 鈥?宸ヨ壓閾捐矾鏃堕棿绾?
1. See-through 鍏ㄨ韩 LayerDiff 1280/30 + 澶撮儴浜屾鎺ㄧ悊  
2. Marigold 娣卞害 鈫?`character.psd`  
3. 渚у埆鏀瑰悕 / 棰勬锛堝凡璀﹀憡 mouth锛? 鐫瘺鎷嗗垎  
4. psd2live mesh 32 / atlas 8192 鈫?moc3  

闂鍦?**姝ラ 1 鐨勬媶灞傝川閲?+ 鍘熺敾闂槾**锛屽湪 **姝ラ 4 缁戦鍚庢毚闇蹭负 VTS 瑙傛劅**銆?
## [S3] Out of Scope

- 涓嶄慨鏀?PSD銆佷笉閲嶈窇 See-through銆佷笉閲嶅 moc3锛堢敤鎴烽€夋嫨浠呰瘖鏂級  
- 涓嶈瘎浠?VTS 鏈韩娓叉煋  
- 涓嶈鐩?test01 妯″瀷  

---

## Tasks

- [x] T1: 瀹氫綅 VTS 妯″瀷涓庢簮 PSD 鈥?acceptance: 璺緞涓庢枃浠舵竻鍗曠‘璁?(covers: S1)
- [x] T2: 閲忓寲 mouth/鐪奸儴浠跺浘灞?鈥?acceptance: 灏哄涓?alpha 缁熻鍐欏叆鎶ュ憡 (covers: S2)
- [x] T3: 鏍稿 blink 鏇茬嚎涓?psd2live 缁戝畾璀﹀憡 鈥?acceptance: 纭鍙傛暟瀛樺湪銆佸垪鍑哄Э鎬佸亸宸?(covers: S2)
- [x] T4: 缁欏嚭鎬诲垽涓庝慨澶嶈竟鐣?鈥?acceptance: 鏄庣‘鈥滅礌鏉愪负涓汇€佸姩鐢讳负鏀惧ぇ鈥?(covers: S2)

---

## 鑻ユ棩鍚庤淇紙鍙傝€冿紝鏈涓嶆墽琛岋級

1. **鎹㈠師鐢?*锛氬槾鐢绘垚鏈€澶у紶鍙ｃ€佽劯閮ㄥ崰姣旀洿澶с€佺溂鍨嬫竻鏅帮紙鎬т环姣旀渶楂橈級銆? 
2. **鎴栨墜宸ユ敼 PSD**锛氳ˉ寮犲彛 mouth锛堝甫鎻忚竟锛夈€侀噸鍋?eyewhite 闀傜┖/瀹屾暣铏硅啘/浠呬笂鐫瘺锛屽啀璺?psd2live銆? 
3. 閲嶅鍚庣敤棰勬纭 mouth 楂樺姣斾笌鍗犻潰閮ㄦ瘮渚嬭揪鏍囷紝鍐嶈繘 VTS銆? 
4. 8GB 鏄惧瓨鏃ュ父寤鸿 768/30锛?280/30 鍦ㄦ湰鏈烘瀬鎱笖瀵光€滃皬鑴糕€濇敹鐩婃湁闄愩€?
## 鐩稿叧璺緞

- VTS 妯″瀷锛歚D:\steam\steamapps\common\VTube Studio\VTube Studio_Data\StreamingAssets\Live2DModels\test02_1280\`  
- 婧?PSD锛歚...\test02_1280\source_psd.psd`  
- 娴佹按绾垮壇鏈細`pipeline-root\jobs\test02\03_psd\character_lash.psd`  
- 璋冭瘯鍥惧眰锛歚pipeline-root\jobs\test02_debug\`  

