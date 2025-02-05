# 检查字符串是否为字母数字

如果你想练习编码，打开终端/SSH 并输入 `node`。下面是一个检查字符串是否仅包含字母数字字符的函数：

```js
const isAlphaNumeric = (str) => /^[a-z0-9]+$/gi.test(str);
```

要使用它，以字符串作为参数调用 `isAlphaNumeric`。如果字符串仅包含字母数字字符，它将返回 `true`，否则返回 `false`。

例如：

```js
isAlphaNumeric("hello123"); // true
isAlphaNumeric("123"); // true
isAlphaNumeric("hello 123"); // false（包含一个空格字符）
isAlphaNumeric("#$hello"); // false（包含非字母数字字符）
```

`RegExp.prototype.test()` 方法用于检查输入字符串是否与字母数字模式匹配，该模式由正则表达式 `/^[a-z0-9]+$/gi` 表示。此模式匹配一个或多个小写字母或数字的任何序列，`g` 和 `i` 标志使匹配不区分大小写。
