---
feature: mobile-batch-app-feasibility
status: delivered
updated: 2026-09-16
branch: (none 鈥?pipeline-root not a git worktree)
commits: n/a
---

# 鎵嬫満绔壒閲忚窇锛氳兘鍚︽墦鍖呮垚 App

## Report

**What was built** 鈥?鍙鎬х粨璁猴細**涓嶈兘鍦ㄦ墜鏈烘湰浣撹窇 See-through/psd2live**锛堜緷璧?NVIDIA CUDA + 澶?GB 鏉冮噸 + 妗岄潰杩愯鏃讹級銆傚彲琛屽舰鎬佹槸銆?*杩欏彴 PC 褰撴湇鍔＄ + 鎵嬫満娴忚鍣ㄦ壒閲忎笂浼?涓嬭浇**銆嶏紝鎴栫函 PC 鎵瑰鐞嗐€?
**Verification** 鈥?瀵圭収鐜版湁鏍堬細see-through-portable锛圕UDA torch锛夈€乸sd2live.exe銆乯pg-to-live2d-workflow锛涘潎涓?Windows 妗岄潰/鏈嶅姟鍣ㄥ舰鎬併€?
**Journey log**
1. 鎵嬫満鏃犲吋瀹?CUDA锛屾棤娉曟湰鍦版帹鐞?LayerDiff/Marigold銆?2. 鐪熸鍙寘瑁呯殑鏄€岄槦鍒?API + 杩涘害 + 浜х墿涓嬭浇銆嶃€?3. 鑻ラ渶鐪熉锋墜鏈?App锛屽彧鑳戒笂浜?GPU锛屾垚鏈笌寤惰繜鍙﹁銆?
---

## [S1] Problem

甯屾湜鍦ㄦ墜鏈虹鎵归噺璺戞暣鍥?鈫?moc3 娴佹按绾裤€?
## [S2] Design

### 涓嶅彲琛?
| 褰㈠紡 | 鍘熷洜 |
|------|------|
| 鍘熺敓 iOS/Android 鏈湴璺?| 鏃?NVIDIA CUDA锛涙ā鍨嬩綋绉笌鍐呭瓨涓嶅尮閰?|
| 鎵嬫満涓婅 see-through-portable | 浠?Windows/Linux + CUDA |

### 鍙鏂规锛堟寜鎺ㄨ崘鎺掑簭锛?
**鏂规 1锛堟帹鑽愶級鈥?鏈満鏈嶅姟 + 鎵嬫満缃戦〉**

```text
鎵嬫満娴忚鍣?  鈫?涓婁紶澶氬紶鍥?  鈫?鏈満 HTTP API 鎺掗槦
  鈫?See-through 768/30 鈫?棰勬 鈫?psd2live
  鈫?鎵嬫満涓嬭浇 zip锛坢oc3 鍏ㄥ锛?```

- 澶嶇敤鐜版湁鑴氭湰锛屽紑鍙戦噺绾︼細闃熷垪銆佷换鍔＄姸鎬併€侀壌鏉冦€佹墦鍖呬笅杞? 
- 鎵归噺锛氫覆琛岋紙8GB 鏄惧瓨涓€娆′竴寮狅級鎴栨瀬灏忓苟鍙? 
- 鎵嬫満鍙槸銆岄仴鎺у櫒銆嶏紝绠楀姏浠嶅湪 PC  

**鏂规 2 鈥?绾?PC 鎵瑰鐞?*

- 鐩綍涓㈠浘 鈫?CLI 寰幆 鈫?`out/<name>/07_model`  
- 涓嶉渶瑕?App锛屼絾涓嶈兘鐢ㄦ墜鏈烘搷浣? 

**鏂规 3 鈥?浜?GPU**

- 鎵嬫満/浠绘剰绔彁浜わ紱闇€绉?GPU銆佷紶澶у浘銆佸悎瑙勪笌璐圭敤  
- 瓒呭嚭鏈満娴佹按绾胯寖鍥? 

### 鎵归噺娉ㄦ剰锛?GB锛?
- 鍚屼竴鏃堕棿 **1 涓?* GPU 浠诲姟  
- 768/30 绾?30鈥?0 鍒嗛挓/寮狅紙鏈満 test03 瀹炴祴 LayerDiff 绾?32min + Marigold 绾?1min锛? 
- 闃熷垪鎸夊簭澶勭悊锛岄伩鍏?OOM  

## [S3] Out of Scope

- 鏈涓嶅疄鐜?App/API锛堜粎缁撹锛? 
- 涓嶄笂浜? 

---

## Tasks

- [x] T1: 缁撹涓庢帹鑽愭灦鏋?鈥?acceptance: 鏂规 1 涓烘帹鑽?(covers: S2)

