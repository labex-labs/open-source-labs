# 将 HSL 转换为数组

要将 `hsl()` 颜色字符串转换为一个值数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `String.prototype.match()` 获取一个包含数值的 3 个字符串的数组。
3. 结合使用 `Array.prototype.map()` 和 `Number` 将它们转换为一个数值数组。

以下是将 `hsl()` 颜色字符串转换为数值数组的代码：

```js
const toHSLArray = (hslStr) => hslStr.match(/\d+/g).map(Number);
```

示例用法：

```js
toHSLArray("hsl(50, 10%, 10%)"); // [50, 10, 10]
```
