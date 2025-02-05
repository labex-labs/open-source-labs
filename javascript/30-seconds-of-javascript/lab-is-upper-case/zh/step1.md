# 检查字符串是否为大写的函数

要检查一个字符串是否为大写，请按以下步骤操作：

1. 打开终端/SSH。
2. 输入 `node`。
3. 使用函数 `isUpperCase()`，通过 `String.prototype.toUpperCase()` 将给定字符串转换为大写，并将其与原始字符串进行比较。
4. 如果字符串为大写，该函数将返回 `true`；如果不是，则返回 `false`。

以下是一个示例代码：

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
