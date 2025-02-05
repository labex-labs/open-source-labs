# 十六进制转 RGB 转换

要将十六进制颜色代码（带或不带 `#` 前缀）转换为 RGB 字符串，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用按位右移运算符，并使用 `&`（与）运算符屏蔽位。
3. 如果颜色代码是 3 位数字，则首先将其转换为 6 位版本。
4. 如果在 6 位十六进制代码旁边提供了 alpha 值，则返回一个 `rgba()` 字符串。

以下是转换的 JavaScript 代码：

```js
const hexToRGB = (hex) => {
  let alpha = false,
    h = hex.slice(hex.startsWith("#") ? 1 : 0);
  if (h.length === 3) h = [...h].map((x) => x + x).join("");
  else if (h.length === 8) alpha = true;
  h = parseInt(h, 16);
  return (
    "rgb" +
    (alpha ? "a" : "") +
    "(" +
    (h >>> (alpha ? 24 : 16)) +
    ", " +
    ((h & (alpha ? 0x00ff0000 : 0x00ff00)) >>> (alpha ? 16 : 8)) +
    ", " +
    ((h & (alpha ? 0x0000ff00 : 0x0000ff)) >>> (alpha ? 8 : 0)) +
    (alpha ? `, ${h & 0x000000ff}` : "") +
    ")"
  );
};
```

你可以使用以下示例调用 `hexToRGB` 函数：

```js
hexToRGB("#27ae60ff"); // 'rgba(39, 174, 96, 255)'
hexToRGB("27ae60"); // 'rgb(39, 174, 96)'
hexToRGB("#fff"); // 'rgb(255, 255, 255)'
```
