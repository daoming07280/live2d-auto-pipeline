---
feature: test03-eye-mouth-diagnosis
status: delivered
updated: 2026-09-16
branch: (none 鈥?pipeline-root not a git worktree)
commits: n/a
---

# test03 鍙崇溂鍙戠櫧 / 闂槾璇″紓 鈥?璇婃柇涓庝慨澶?
## Report

**What was built** 鈥?瀹氫綅 test03锛?*鍙崇溂琚溂鐧藉眰鐩栦綇鐬冲瓟**锛圥SD 涓?`eyewhite-r` 鍦?`irides-r` 涔嬩笂锛夛紱**鍚庡彂鍦ㄦ暣鏍堟渶涓?*瀵艰嚧鍚堟垚椤哄簭寮傚父銆傚凡閲嶆帓灞傚簭骞堕噸瀵煎嚭涓?`models/test03_768_v2`銆傚槾涓哄悎鏍煎紶鍙ｅ浘锛?2脳46锛屾瘮 1.10锛夛紝闂槾璇″紓灞炪€屽紶鍙ｅ浘鍚戜腑绾垮帇缂┿€嶇殑绠楁硶鍥烘湁瑙傛劅锛屼笉鏄病缁戝弬鏁般€?
**Verification** 鈥?鎵嬪伐鎸夋纭簭鍚堟垚 v2锛氬弻鐪奸潚缁胯櫣鑶滃彲瑙併€佸槾寮犲紑锛沗psd_precheck` 閫氳繃锛沗vts_check` 鏃犻樆鏂€?
**Journey log**
1. See-through 杈撳嚭鐨?PSD 灞傚簭涓嶇ǔ瀹氾紙鍚庡彂鍙兘鍦ㄦ渶涓娿€佸乏鍙崇溂鐧?鐬冲瓟鐩稿椤哄簭涓嶄竴鑷达級銆?2. 鍙崇溂锛歟yewhite-r 鍘嬪湪 irides-r 涓?鈫?鍙鐪肩櫧銆?3. 閲嶆帓 `back hair 鈫?鈥?鈫?eyewhite 鈫?irides 鈫?lash 鈫?front hair` 鍚庢甯搞€?4. 寮犲彛鍥惧帇鎴愰棴鍙ｄ粛浼氥€岃寮傘€嶏紝灞?psd2live 褰㈠彉闄愬埗銆?
---

## [S1] Problem

VTS 涓?test03锛氬彸鐪煎叏鐧斤紱鍢磋瘑鍒笉鐏垫晱銆侀棴鍢磋寮傘€?
## [S2] Design

### 鍙崇溂鍏ㄧ櫧

| 椤?| v1 閿欒搴?| v2 淇 |
|----|-----------|---------|
| irides-r vs eyewhite-r | 鐪肩櫧鍦ㄧ灣瀛斾箣涓?| 鐬冲瓟鍦ㄧ溂鐧戒箣涓?|
| back hair | 鍙兘鍦ㄦ暣鏍堥敊璇綅缃?| 缃簬搴曞眰 |

鐬冲瓟鍥惧眰鏈韩璐ㄩ噺姝ｅ父锛堥潚缁胯櫣鑶滐級銆傚睘 **PSD 缁樺埗椤哄簭 / 灞傚簭** 闂锛屼笉鏄己 irides銆?
### 鍢?
- mouth **42脳47**锛岄妫€閫氳繃锛堝紶鍙ｅ悎鏍硷級  
- 銆屼笉鐏垫晱 / 闂笂璇″紓銆嶏細psd2live 鐢?*鏈€澶у紶鍙?*鍚戜腑绾垮帇缂╂ā鎷熼棴鍙ｏ紝鍞囧唴鑹插潡鎸ゆ垚涓€鏉＄嚎锛屽睘绠楁硶瑙傛劅闂  
- 鍙傛暟 `ParamMouthOpenY` / LipSync 缁勫凡瀛樺湪  

### 浜х墿

- 淇鍖咃細`pipeline-root\models\test03_768_v2\`  
- 鏃у寘 `test03_768` 鍙純鐢? 

## [S3] Out of Scope

- 涓嶉噸璺?See-through  
- 涓嶆敼 psd2live 绠楁硶  

---

## Tasks

- [x] T1: 璇婃柇灞傚簭涓庡槾灏哄 鈥?acceptance: 鏍瑰洜鏄庣‘ (covers: S2)
- [x] T2: 閲嶆帓 PSD 骞堕噸瀵煎嚭 鈥?acceptance: v2 鍙岀溂铏硅啘鍙 + vts_check 閫氳繃 (covers: S2)

