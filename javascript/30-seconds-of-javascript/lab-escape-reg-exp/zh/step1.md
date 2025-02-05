# 如何在 JavaScript 中转义正则表达式

要在 JavaScript 中对字符串进行转义以便在正则表达式中使用，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `String.prototype.replace()` 对特殊字符进行转义。
3. 复制并粘贴以下代码片段：

```js
const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
```

4. 使用 `escapeRegExp()` 函数对字符串中的特殊字符进行转义。

以下是一个示例：

```js
escapeRegExp("(test)"); // \\(test\\)
```

通过这些步骤，你现在可以轻松地在 JavaScript 正则表达式中转义任何特殊字符。
