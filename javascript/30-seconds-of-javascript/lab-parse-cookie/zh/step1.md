# 用于解析 HTTP Cookie 的 JavaScript 函数

要在 JavaScript 中解析 HTTP Cookie 头字符串并返回所有 cookie 名值对的对象，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `String.prototype.split()` 将键值对彼此分开。
- 使用 `Array.prototype.map()` 和 `String.prototype.split()` 在每对中分离键和值。
- 使用 `Array.prototype.reduce()` 和 `decodeURIComponent()` 创建一个包含所有键值对的对象。

以下是实现上述步骤的 `parseCookie()` 函数的示例：

```js
const parseCookie = (str) =>
  str
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});
```

你可以按如下方式测试该函数：

```js
parseCookie("foo=bar; equation=E%3Dmc%5E2");
// { foo: 'bar', equation: 'E=mc^2' }
```
