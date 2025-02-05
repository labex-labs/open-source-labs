# 换行字符串的说明

要进行编码练习，请打开终端/SSH 并输入 `node`。

此代码使用换行符将字符串换行到指定的字符数。使用方法如下：

1. 使用 `String.prototype.replace()` 和正则表达式在距离 `max` 个字符最近的空白处插入指定的换行符。
2. 如果你不想使用第三个参数 `br` 的默认值 `'\n'`，可以省略它并提供自己的字符。

以下是代码：

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

以下是一些使用示例：

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
