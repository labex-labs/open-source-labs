# 如何序列化一个 Cookie

要开始练习编码，请打开终端/SSH 并输入`node`。然后，按照以下步骤将一个 Cookie 名值对序列化为一个 Set-Cookie 头字符串：

1. 使用模板字面量和`encodeURIComponent()`来创建合适的字符串。
2. 通过传入`name`和`val`参数来实现`serializeCookie`函数。
3. 该函数将返回一个正确序列化的字符串。

以下是如何使用`serializeCookie`函数的示例：

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

在这个示例中，`serializeCookie`函数将`foo`作为 Cookie 名称，`bar`作为 Cookie 值，并返回一个序列化后的 Cookie 字符串`foo=bar`。
