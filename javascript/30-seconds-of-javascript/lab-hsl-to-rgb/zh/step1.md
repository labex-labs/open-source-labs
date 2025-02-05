# 使用 JavaScript 将 HSL 转换为 RGB

要将 HSL 格式的颜色元组转换为 RGB，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 [HSL 到 RGB 的转换公式](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB) 将颜色元组转换为适当的格式。
3. 确保输入参数在以下范围内：H：[0, 360]，S：[0, 100]，L：[0, 100]。
4. 输出值应在 [0, 255] 范围内。

以下是 HSL 到 RGB 转换公式的 JavaScript 代码：

```js
const HSLToRGB = (h, s, l) => {
  s /= 100;
  l /= 100;
  const k = (n) => (n + h / 30) % 12;
  const a = s * Math.min(l, 1 - l);
  const f = (n) =>
    l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
  return [255 * f(0), 255 * f(8), 255 * f(4)];
};
```

要使用该函数，请将 H、S 和 L 值作为参数提供：

```js
HSLToRGB(13, 100, 11); // [56.1, 12.155, 0]
```
