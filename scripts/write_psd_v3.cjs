const fs = require('fs');
const path = require('path');
const agPsd = require('<PIPELINE_ROOT>/jpg-to-live2d-workflow/node_modules/ag-psd');
const rawDir = process.argv[2];
const outPsd = process.argv[3];
const meta = JSON.parse(fs.readFileSync(path.join(rawDir, 'meta.json'), 'utf8'));
// meta.layers is bottom -> top draw order; ag-psd children[0] = first drawn = bottom
const children = meta.layers.map((l) => {
  const buf = fs.readFileSync(path.join(rawDir, l.raw));
  return {
    name: l.name,
    top: 0,
    left: 0,
    bottom: l.h,
    right: l.w,
    imageData: {
      width: l.w,
      height: l.h,
      data: new Uint8ClampedArray(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength))
    }
  };
});
const out = agPsd.writePsdBuffer({ width: meta.w, height: meta.h, children }, { generateThumbnail: false });
fs.writeFileSync(outPsd, out);
console.log('wrote', outPsd, out.length, 'layers', children.length);

