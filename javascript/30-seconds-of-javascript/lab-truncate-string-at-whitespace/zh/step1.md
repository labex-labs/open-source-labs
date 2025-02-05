# 如何在 JavaScript 中按空白字符截断字符串

要进行编码练习，请打开终端/SSH 并输入 `node`。

以下是一个函数，它会在尽可能尊重空白字符的情况下，将字符串截断到指定长度：

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

要使用此函数，请将你想要截断的字符串作为第一个参数传入，将最大长度作为第二个参数传入，并将一个可选的结尾字符串作为第三个参数传入。如果字符串的长度小于或等于指定的限制，则返回原始字符串。否则，该函数将在限制之前找到最后一个空格，并在该位置截断字符串，如果指定了结尾字符串，则添加结尾字符串。

以下是一些示例：

```js
truncateStringAtWhitespace("short", 10); // 'short'
truncateStringAtWhitespace("not so short", 10); // 'not so...'
truncateStringAtWhitespace("trying a thing", 10); // 'trying...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
