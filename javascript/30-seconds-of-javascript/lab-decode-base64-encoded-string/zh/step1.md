# 解码Base64编码字符串

要解码使用Base64编码的一串数据，请执行以下步骤：

1. 打开终端/SSH并输入`node`以开始练习编码。
2. 为给定的Base64编码字符串创建一个`Buffer`。
3. 使用`Buffer.prototype.toString()`返回解码后的字符串。

以下是一个示例代码片段：

```js
const atob = (str) => Buffer.from(str, "base64").toString("binary");
```

你可以通过运行`atob('Zm9vYmFy')`来测试此函数，它应该返回`'foobar'`。
