# RGB 转 HSL 转换

要将 RGB 颜色元组转换为 HSL 格式，请执行以下步骤：

1. 打开终端/SSH 开始练习编码。
2. 输入 `node` 并按回车键。
3. 使用 [RGB 到 HSL 的转换公式](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/) 转换为适当的格式。
4. 确保所有输入参数都在 [0, 255] 范围内。
5. 结果值应在以下范围内：H: [0, 360]，S: [0, 100]，L: [0, 100]。

以下是 JavaScript 中 RGBToHSL 函数的示例：

```js
const RGBToHSL = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const l = Math.max(r, g, b);
  const s = l - Math.min(r, g, b);
  const h = s
    ? l === r
      ? (g - b) / s
      : l === g
        ? 2 + (b - r) / s
        : 4 + (r - g) / s
    : 0;
  return [
    60 * h < 0 ? 60 * h + 360 : 60 * h,
    100 * (s ? (l <= 0.5 ? s / (2 * l - s) : s / (2 - (2 * l - s))) : 0),
    (100 * (2 * l - s)) / 2
  ];
};
```

以下是如何使用 RGBToHSL 函数的示例：

```js
RGBToHSL(45, 23, 11); // [21.17647, 60.71428, 10.98039]
```
