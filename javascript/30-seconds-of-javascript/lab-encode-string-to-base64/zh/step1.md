# 将字符串编码为 Base64

要将一个 String 对象编码为 Base64 编码的 ASCII 字符串，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始编码。
2. 使用给定的字符串和二进制编码创建一个 `Buffer`。
3. 使用 `Buffer.prototype.toString()` 返回 Base64 编码的字符串。

以下是一个示例代码片段：

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

现在你可以使用 `encodeToBase64()` 函数将任何字符串编码为 Base64。例如：

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
