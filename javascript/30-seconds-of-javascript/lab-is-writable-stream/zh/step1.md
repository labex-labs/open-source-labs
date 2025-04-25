# 检查流是否可写

要检查一个流是否可写，请打开终端/SSH 并输入 `node` 以开始练习编码。然后，按照以下步骤操作：

1. 检查给定的参数是否不为 `null`。
2. 使用 `typeof` 检查该值是否为 `object` 类型，以及 `pipe` 属性是否为 `function` 类型。
3. 此外，检查 `_write` 和 `_writableState` 属性的 `typeof` 是否分别为 `function` 和 `object` 类型。

以下是实现这些检查的示例代码：

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

你可以使用 Node.js 中的 `fs` 模块来测试此函数。例如：

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
