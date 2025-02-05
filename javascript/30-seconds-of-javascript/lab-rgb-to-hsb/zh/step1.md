# RGB 转 HSB 转换

要将 RGB 颜色元组转换为 HSB 格式，你可以按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 [RGB 到 HSB 的转换公式](https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB) 将 RGB 颜色元组转换为适当的 HSB 格式。
3. 输入参数范围是 [0, 255]，而结果值的范围是：

- H：[0, 360]
- S：[0, 100]
- B：[0, 100]

以下是 JavaScript 中的函数：

```js
const RGBToHSB = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const v = Math.max(r, g, b),
    n = v - Math.min(r, g, b);
  const h =
    n === 0
      ? 0
      : n && v === r
        ? (g - b) / n
        : v === g
          ? 2 + (b - r) / n
          : 4 + (r - g) / n;
  return [60 * (h < 0 ? h + 6 : h), v && (n / v) * 100, v * 100];
};
```

你可以这样调用该函数：

```js
RGBToHSB(252, 111, 48);
// [18.529411764705856, 80.95238095238095, 98.82352941176471]
```
