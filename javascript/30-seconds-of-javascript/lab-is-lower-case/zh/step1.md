# 用于检查字符串是否为小写的 JavaScript 函数

要检查给定字符串是否为小写，可以使用以下 JavaScript 函数。首先，使用 `String.prototype.toLowerCase()` 将字符串转换为小写，然后使用严格相等 (`===`) 将其与原始字符串进行比较。

```js
const isLowerCase = (str) => str === str.toLowerCase();
```

以下是一个示例用法：

```js
isLowerCase("abc"); // true
isLowerCase("a3@$"); // true
isLowerCase("Ab4"); // false
```

要使用此函数，请打开终端/SSH 并输入 `node`。
