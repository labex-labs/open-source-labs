# 如何在终端/SSH 中开始练习编码

要在终端/SSH 中开始练习编码，只需输入 `node`。

# 将多行字符串拆分为行数组

要将多行字符串拆分为行数组：

- 使用 `String.prototype.split()` 和正则表达式来匹配换行符并创建一个数组。
- 正则表达式 `/\r?\n/` 匹配 `\r` 和 `\n` 两种换行符。
- 这将返回一个行数组。

```js
const splitLines = (str) => str.split(/\r?\n/);
```

```js
splitLines("This\nis a\nmultiline\nstring.\n");
// ['This', 'is a','multiline','string.', '']
```
