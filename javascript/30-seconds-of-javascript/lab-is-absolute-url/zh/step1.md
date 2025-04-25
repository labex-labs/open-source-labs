# 检查字符串是否为绝对 URL 的函数

要检查给定的字符串是否为绝对 URL，请执行以下步骤：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用`RegExp.prototype.test()`来测试字符串是否为绝对 URL。
3. 函数应定义为`const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);`
4. 该函数接受一个字符串参数`str`，如果字符串是绝对 URL，则返回`true`，否则返回`false`。
5. 使用提供的示例测试该函数：

```js
isAbsoluteURL("https://google.com"); // true
isAbsoluteURL("ftp://www.myserver.net"); // true
isAbsoluteURL("/foo/bar"); // false
```
