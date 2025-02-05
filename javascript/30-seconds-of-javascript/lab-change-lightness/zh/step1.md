# 如何更改 HSL 颜色的亮度

要更改 `hsl()` 颜色字符串的亮度值，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。

2. 使用 `String.prototype.match()` 获取一个包含三个字符串的数组，这些字符串来自 `hsl()` 字符串中的数值。

3. 结合使用 `Array.prototype.map()` 和 `Number` 将字符串转换为数值数组。

4. 使用 `Math.max()` 和 `Math.min()` 确保亮度值落在有效范围内（介于 `0` 和 `100` 之间）。

5. 使用模板字面量创建一个新的 `hsl()` 字符串，其中包含更新后的亮度值。

以下是实现这些步骤的示例代码片段：

```js
const changeLightness = (delta, hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);

  const newLightness = Math.max(
    0,
    Math.min(100, lightness + parseFloat(delta))
  );

  return `hsl(${hue}, ${saturation}%, ${newLightness}%)`;
};
```

然后，你可以使用一个增量值和一个 `hsl()` 字符串调用 `changeLightness()` 函数，以获取一个包含更新后亮度值的新 `hsl()` 字符串。例如：

```js
changeLightness(10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 60%)'
changeLightness(-10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 40%)'
```
