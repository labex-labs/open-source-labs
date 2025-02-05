# URL 片段连接与规范化

要将给定的 URL 片段连接在一起并规范化生成的 URL，请遵循以下步骤：

1. 使用 `Array.prototype.join()` 来组合 URL 片段。
2. 使用一系列 `String.prototype.replace()` 调用以及各种正则表达式来规范化生成的 URL，方法如下：
   - 去除双斜杠
   - 为协议添加适当的斜杠
   - 去除参数前的斜杠
   - 使用 `'&'` 组合参数并规范化第一个参数分隔符。

使用以下代码片段来连接和规范化 URL 片段：

```js
const URLJoin = (...args) =>
  args
    .join("/")
    .replace(/[\/]+/g, "/")
    .replace(/^(.+):\//, "$1://")
    .replace(/^file:/, "file:/")
    .replace(/\/(\?|&|#[^!])/g, "$1")
    .replace(/\?/g, "&")
    .replace("&", "?");
```

示例用法：

```js
URLJoin("http://www.google.com", "a", "/b/cd", "?foo=123", "?bar=foo");
// 'http://www.google.com/a/b/cd?foo=123&bar=foo'
```
