# 检查字符串是否仅包含字母的函数

要检查一个字符串是否仅包含字母字符：

- 打开终端/SSH 并输入`node`以开始练习编码。
- 使用`RegExp.prototype.test()`来检查给定字符串是否与字母正则表达式模式匹配。
- 函数`isAlpha`接受一个字符串作为参数，如果字符串仅包含字母字符则返回`true`，否则返回`false`。

以下是一个示例：

```js
const isAlpha = (str) => /^[a-zA-Z]*$/.test(str);
```

```js
isAlpha("sampleInput"); // true
isAlpha("this Will fail"); // false
isAlpha("123"); // false
```
