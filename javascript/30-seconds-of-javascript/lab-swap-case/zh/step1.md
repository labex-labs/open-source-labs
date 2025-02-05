# 如何在JavaScript中交换字符串的大小写

要在JavaScript中交换字符串的大小写，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用展开运算符（`...`）将输入字符串 `str` 转换为字符数组。
3. 使用 `String.prototype.toLowerCase()` 和 `String.prototype.toUpperCase()` 将小写字符转换为大写，反之亦然。
4. 使用 `Array.prototype.map()` 将转换应用于每个字符，并使用 `Array.prototype.join()` 将字符组合回字符串。
5. 请注意，将字符串的大小写交换两次不一定会得到原始字符串。

以下是一个示例代码片段，展示了如何在JavaScript中交换字符串的大小写：

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // 输出: 'hELLO WORLD!'
```
