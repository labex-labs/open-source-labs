# 用于缩进 JavaScript 字符串的函数

要在给定字符串的每一行添加缩进，可以使用 JavaScript 中的 `indentString()` 函数。此函数接受三个参数：`str`、`count` 和 `indent`。

- `str` 参数表示要缩进的字符串。
- `count` 参数确定要缩进每一行的次数。
- `indent` 参数是可选的，表示要用于缩进的字符。如果不提供它，默认值是单个空格字符（`' '`）。

以下是 `indentString()` 函数的代码：

```js
const indentString = (str, count, indent = " ") =>
  str.replace(/^/gm, indent.repeat(count));
```

要使用此函数，只需使用所需的参数调用它。以下是一些示例：

```js
indentString("Lorem\nIpsum", 2); // '  Lorem\n  Ipsum'
indentString("Lorem\nIpsum", 2, "_"); // '__Lorem\n__Ipsum'
```

在第一个示例中，`indentString('Lorem\nIpsum', 2)` 返回 `'  Lorem\n  Ipsum'`，这意味着输入字符串的每一行都用空格字符缩进了两次。

在第二个示例中，`indentString('Lorem\nIpsum', 2, '_')` 返回 `'__Lorem\n__Ipsum'`，这意味着输入字符串的每一行都用下划线字符（`'_'`）缩进了两次。
