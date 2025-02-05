# 如何在 JavaScript 中把每个单词的首字母大写

要使用 JavaScript 将字符串中的每个单词的首字母大写，你可以使用 `String.prototype.replace()` 方法来匹配每个单词的首字母，然后使用 `String.prototype.toUpperCase()` 方法将其大写。

以下是一个你可以使用的示例代码片段：

```js
const capitalizeEveryWord = (str) =>
  str.replace(/\b[a-z]/g, (char) => char.toUpperCase());
```

要使用此函数，将你想要大写的字符串作为参数传入，如下所示：

```js
capitalizeEveryWord("hello world!"); // 'Hello World!'
```

这将返回大写后的字符串 'Hello World!'。
