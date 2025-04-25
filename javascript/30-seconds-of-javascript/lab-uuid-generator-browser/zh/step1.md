# 在浏览器中生成 UUID

要在浏览器中生成符合 [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) 版本 4 的 UUID，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node`。
2. 使用 `Crypto.getRandomValues()` 方法生成 UUID。
3. 使用 `Number.prototype.toString()` 方法将 UUID 转换为十六进制字符串。
4. 实现以下代码：

```js
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. 调用 `UUIDGeneratorBrowser()` 函数生成 UUID。例如，`UUIDGeneratorBrowser()` 将返回 `'7982fcfe-5721-4632-bede-6000885be57d'`。
