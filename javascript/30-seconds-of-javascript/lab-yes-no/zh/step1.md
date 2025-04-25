# 检查是/否字符串的函数

要检查一个字符串是否为“是”或“否”的答案，请在终端/SSH 中通过输入`node`使用以下函数：

```js
const yesNo = (val, def = false) =>
  /^(y|yes)$/i.test(val) ? true : /^(n|no)$/i.test(val) ? false : def;
```

- 如果字符串为“y”/“yes”，则函数返回`true`；如果字符串为“n”/“no”，则返回`false`。
- 若要设置默认答案，请省略第二个参数`def`。默认情况下，函数将返回`false`。
- 该函数使用`RegExp.prototype.test()`来检查字符串是否匹配“y”/“yes”或“n”/“no”。

示例用法：

```js
yesNo("Y"); // true
yesNo("yes"); // true
yesNo("No"); // false
yesNo("Foo", true); // true
```
