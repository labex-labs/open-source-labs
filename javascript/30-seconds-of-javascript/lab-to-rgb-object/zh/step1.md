# 将 RGB 转换为对象

要将 `rgb()` 颜色字符串转换为一个包含每种颜色值的对象，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `String.prototype.match()` 获取一个包含三个数值字符串的数组。
3. 结合使用 `Array.prototype.map()` 和 `Number` 将它们转换为一个数值数组。
4. 使用数组解构将这些值存储到命名变量中，并从中创建一个合适的对象。

以下是你可以使用的代码：

```js
const toRGBObject = (rgbStr) => {
  const [red, green, blue] = rgbStr.match(/\d+/g).map(Number);
  return { red, green, blue };
};

toRGBObject("rgb(255, 12, 0)"); // {red: 255, green: 12, blue: 0}
```
