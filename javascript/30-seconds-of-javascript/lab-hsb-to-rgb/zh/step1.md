# HSB 转 RGB 转换

要将 HSB 颜色元组转换为 RGB 格式，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 开始练习编码。
- 使用 [HSB 到 RGB 的转换公式](https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB) 转换为适当的格式。
- 输入参数应在以下范围内：H: [0, 360]，S: [0, 100]，B: [0, 100]。
- 所有输出值应在 [0, 255] 范围内。

以下是可用于将 HSB 转换为 RGB 的代码：

```js
const HSBToRGB = (h, s, b) => {
  s /= 100;
  b /= 100;
  const k = (n) => (n + h / 60) % 6;
  const f = (n) => b * (1 - s * Math.max(0, Math.min(k(n), 4 - k(n), 1)));
  return [255 * f(5), 255 * f(3), 255 * f(1)];
};
```

例如，如果你想将 HSB 颜色元组 (18, 81, 99) 转换为 RGB 格式，可以使用以下代码：

```js
HSBToRGB(18, 81, 99); // [252.45, 109.31084999999996, 47.965499999999984]
```
