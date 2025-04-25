# 检查流是否可读

要检查给定参数是否为可读流，请执行以下步骤：

- 首先，打开终端/SSH 并输入 `node` 以开始练习编码。
- 检查该值是否不为 `null`。
- 使用 `typeof` 检查该值是否为 `object` 且 `pipe` 属性是否为 `function`。
- 此外，检查 `_read` 和 `_readableState` 属性的 `typeof` 是否分别为 `function` 和 `object`。

以下是一个实现这些步骤的示例函数：

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

你可以使用此函数检查流是否可读，如下所示：

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
