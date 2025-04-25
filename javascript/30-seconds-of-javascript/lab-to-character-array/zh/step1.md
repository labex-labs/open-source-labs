# 如何在 JavaScript 中将字符串转换为字符数组

要在 JavaScript 中将字符串转换为字符数组，请执行以下步骤：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用展开运算符（`...`）将字符串转换为字符数组。
3. 定义一个名为`toCharArray`的函数，该函数将字符串作为参数，并返回其字符数组。
4. 使用要转换的字符串作为参数调用`toCharArray`函数。
5. 该函数将返回一个字符数组。

以下是代码：

```js
const toCharArray = (s) => [...s];

toCharArray("hello"); // ['h', 'e', 'l', 'l', 'o']
```
