---
feature: design-sheet-to-psd-feasibility
status: delivered
updated: 2026-09-16
branch: (none 鈥?pipeline-root is not a git worktree)
commits: n/a
---

# 瑙掕壊璁惧畾鍥捐兘鍚︾洿鎺ョ敓鎴?Live2D PSD

## Report

**What was built** 鈥?鍙鎬х粨璁猴細杈撳叆涓恒€屽皬椴搁奔濞樸€嶈瀹氭嫾鐗堬紙1536脳1024 RGB锛夛紝涓嶈兘鐩存帴鍙樻垚鍙粦楠ㄧ殑鍒嗗眰 PSD锛汫itHub 鏈彂鐜颁紭浜庣幇鏈夋祦姘寸嚎鐨勪笓鐢ㄥ紑婧愰」鐩紱鐢ㄦ埛閫夋嫨涓嶉儴缃层€佷笉鏀归€犮€?
**Verification** 鈥?璇诲彇鍥剧墖灏哄/妯″紡锛涚洏鐐规湰鏈?`compose_psd.py`銆乣psd_fix_layers` / `precheck` / `split_lash`銆乸sd2live锛汫itHub 妫€绱?character sheet / parts 鈫?PSD 鐩稿叧浠撳簱銆?
**Journey log**
1. 璁惧畾鍥炬槸閮ㄤ欢**鍙傝€冪缉鐣?*锛屼笉鏄富瑙掕壊鐢诲竷涓婄殑瀵归綈閫忔槑灞傘€?2. 鐜版湁閾捐矾宸茶鐩栥€屽垎灞?PNG 鈫?PSD 鈫?moc3銆嶏紱缂虹殑鏄悎鏍煎垎灞傛簮锛屼笉鏄己涓€涓柊浠撳簱銆?3. `design-to-psd` 绛夊亸璁捐绋块噸寤猴紝涓嶉€傚悎浜屾鍏冨彲鍔ㄥ眰銆?
---

## [S1] Problem

鐢ㄦ埛闂細缁欏畾宸叉媶濂界殑璁惧畾鍥撅紝鑳藉惁鐩存帴鐢熸垚 PSD锛涜嫢涓嶈兘锛屾槸鍚﹀簲鍦?GitHub 鎵鹃」鐩苟閮ㄧ讲鍒版祦姘寸嚎鐩綍銆?
## [S2] Design锛堢粨璁猴級

### 涓嶈兘鐩存帴鐢熸垚鐨勫師鍥?
| 鏉′欢 | 璁惧畾鍥剧幇鐘?| Live2D/psd2live 闇€瑕?|
|------|------------|----------------------|
| 甯冨眬 | 鍏ㄨ韩 + 渚ц + 琛ㄦ儏鏉?+ 閮ㄤ欢灏忓浘鎷肩増 | 鍚勯儴浠跺湪鍚屼竴鐢诲竷鍧愭爣 |
| 閫忔槑 | 鏁撮〉涓嶉€忔槑 RGB | 姣忓眰鐙珛 alpha |
| 鍒嗚鲸鐜?| 閮ㄤ欢澶氫负缂╃暐 | 涓庣珛缁樺悓绾у儚绱?|
| 璇箟 | 鍙傝€冨浘锛岄潪宸ョ▼灞?| `face` / `eyewhite` / `mouth`(寮犲彛) / `front hair`鈥?|

瑁佸垏璁惧畾鍥?*涓嶈兘**寰楀埌鍙粦楠ㄦ簮锛涙渶澶氬緱鍒般€屽弬鑰冪敤銆嶆嫾璐淬€?
### 鏈満宸插叿澶囷紙鏃犻渶鏂伴儴缃诧級

- `jpg-to-live2d-workflow/compose_psd.py` + `.venv-psd`锛圥illow + psd-tools锛? 
- `psd_fix_layers` / `psd_precheck` / `psd_split_lash`  
- psd2live 渚挎惡鐗?鈫?moc3  

杈撳叆浠嶆槸锛?*瀵归綈鍚庣殑鍒嗗眰 PNG 鎴栬鑼?PSD**銆?
### GitHub 妫€绱㈡憳瑕?
- 鏈彂鐜版垚鐔熺殑銆岃鑹茶瀹氬浘 鈫?Live2D 鍒嗗眰 PSD銆嶄笓鐢ㄩ」鐩€? 
- 鐩稿叧澶氫负锛歱sd2live锛圥SD鈫抦oc3锛夈€丼ee-through锛堟暣鍥炬媶灞傦級銆乨esign-to-psd锛堝钩闈㈣璁＄锛夈€? 
- 鐢ㄦ埛鎸囧畾銆屽彧瑕佺粨璁轰笉閮ㄧ讲銆嶁啋 **涓?clone銆佷笉瀹夎銆?*

### 鑻ヨ鍙敤妯″瀷鐨勬帹鑽愯矾寰?
1. 鎻愪緵**鐪熸鍒嗗眰**鐨?PSD/PNG锛堢敾甯堝伐绋嬶級锛屾垨  
2. 鍙敤璁惧畾鍥句腑**涓ぎ鍏ㄨ韩鍍?*鍋?See-through 鎷嗗眰锛堥儴浠跺弬鑰冧笉鐩存帴褰撳眰锛夛紝鍐嶉妫€ 鈫?psd2live銆? 

鍢撮渶涓烘渶澶у紶鍙ｏ紱鐪肩櫧/鐬冲瓟/涓婄潾姣涢渶鍒嗗眰娓呮櫚銆?
## [S3] Out of Scope

- 涓嶉儴缃叉柊 GitHub 椤圭洰  
- 涓嶄粠璁惧畾鍥捐嚜鍔ㄦ姞鐢熶骇灞? 
- 涓嶉噸璺?GPU 鎷嗗眰 / 涓嶆敼鐜版湁妯″瀷  

---

## Tasks

- [x] T1: 鏍稿疄杈撳叆鍥炬€ц川 鈥?acceptance: 纭鎷肩増鍙傝€冨浘銆侀潪瀵归綈鍒嗗眰婧?(covers: S2)
- [x] T2: 鐩樼偣鏈満 PSD 鑳藉姏 鈥?acceptance: compose/棰勬/psd2live 宸插瓨鍦?(covers: S2)
- [x] T3: GitHub 妫€绱㈠苟缁欏嚭缁撹 鈥?acceptance: 鏃犲繀瑁呮柊椤圭洰锛涙寜鐢ㄦ埛瑕佹眰涓嶉儴缃?(covers: S2)

