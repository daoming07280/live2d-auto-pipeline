# test03 诊断：右眼发白 / 脸颊耳朵 / 嘴唇缺失

## 右眼全白

PSD 中 `eyewhite-r` 画在 `irides-r` 之上，瞳孔被眼白盖住。

修复：重排为 eyewhite → irides → eyelash。

## 脸颊耳朵

See-through 将完整人耳误检到右脸颊（`ears-r` 完全落在脸内）。

修复：删除 `ears-r`；侧边 `ears-l` 若在脸轮廓外可保留。

## 嘴唇缺失

原 mouth 层几乎只有口腔内部，无上下唇。

修复：用原图在嘴部 ROI 重采，保留唇线与张口内部。

预检：mouth 约 78×83，高宽比约 1.06。

## 闭嘴诡异

psd2live 将最大张口向中线压缩模拟闭口，属算法观感问题。

自然闭口需 `mouth_close` 差分或 Cubism 精修。

## 产物

`results/test03_768_v3/`（层序 + 去耳 + 嘴部重采后导出）。
