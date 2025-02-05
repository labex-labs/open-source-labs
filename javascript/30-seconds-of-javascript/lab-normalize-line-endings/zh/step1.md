# 规范化行尾的函数

要规范化字符串中的行尾，你可以使用以下函数。

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- 使用 `String.prototype.replace()` 和正则表达式来匹配行尾，并将其替换为 `normalized` 版本。
- 默认情况下，`normalized` 版本设置为 `'\r\n'`。
- 要使用不同的 `normalized` 版本，将其作为第二个参数传递。

以下是一些示例：

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
