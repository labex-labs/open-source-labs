# 如何序列化一个Cookie

要开始练习编码，请打开终端/SSH并输入`node`。然后，按照以下步骤将一个Cookie名值对序列化为一个Set-Cookie头字符串：

1. 使用模板字面量和`encodeURIComponent()`来创建合适的字符串。
2. 通过传入`name`和`val`参数来实现`serializeCookie`函数。
3. 该函数将返回一个正确序列化的字符串。

以下是如何使用`serializeCookie`函数的示例：

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

在这个示例中，`serializeCookie`函数将`foo`作为Cookie名称，`bar`作为Cookie值，并返回一个序列化后的Cookie字符串`foo=bar`。
