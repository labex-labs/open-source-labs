# 用于填充字符串的函数

要在字符串两侧用指定字符进行填充（如果字符串长度小于指定的 `length`），可使用以下函数：

```js
const pad = (str, length, char = " ") =>
  str.padStart((str.length + length) / 2, char).padEnd(length, char);
```

该函数使用 `String.prototype.padStart()` 和 `String.prototype.padEnd()` 来填充给定字符串的两侧。你可以省略第三个参数 `char`，以使用空白字符作为默认的填充字符。

以下是一些使用 `pad()` 函数的示例：

```js
pad("cat", 8); // '  cat   '
pad(String(42), 6, "0"); // '004200'
pad("foobar", 3); // 'foobar'
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
