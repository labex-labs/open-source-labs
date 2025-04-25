# 在 Node.js 中生成 UUID

要在 Node.js 中生成 UUID，请按照以下步骤操作：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用`crypto.randomBytes()`方法生成符合[RFC4122](https://www.ietf.org/rfc/rfc4122.txt)第 4 版的 UUID。
3. 使用`Number.prototype.toString()`方法将生成的 UUID 转换为合适的 UUID（十六进制字符串）。
4. 或者，你可以使用提供类似功能的[`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions)方法。

以下是在 Node.js 中生成 UUID 的示例代码片段：

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );
```

你可以调用`UUIDGeneratorNode()`方法来生成 UUID。

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
