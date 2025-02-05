# 将 RGB 字符串转换为数组

要将 `rgb()` 颜色字符串转换为值数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `String.prototype.match()` 获取一个包含数值的 3 个字符串的数组。
3. 将 `Array.prototype.map()` 与 `Number` 结合使用，将它们转换为数值数组。

以下是你可以使用的代码：

```js
const toRGBArray = (rgbStr) => rgbStr.match(/\d+/g).map(Number);
```

要测试该函数，请使用 `rgb()` 颜色字符串作为参数调用它，如下所示：

```js
toRGBArray("rgb(255, 12, 0)"); // [255, 12, 0]
```
