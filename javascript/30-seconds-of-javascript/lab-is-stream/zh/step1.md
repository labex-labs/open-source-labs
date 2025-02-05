# 如何在Node.js中检查一个值是否为流

要在Node.js中检查一个值是否为流，你可以使用 `isStream` 函数。使用此函数，请按以下步骤操作：

1. 打开终端/SSH。
2. 输入 `node` 开始练习编码。
3. 使用 `isStream` 函数检查给定参数是否为流。
4. 要检查该值是否不等于 `null`，请使用以下代码：

```js
const isStream = (val) =>
  val !== null && typeof val === "object" && typeof val.pipe === "function";
```

5. 要检查一个文件是否为流，请使用以下代码：

```js
const fs = require("fs");

isStream(fs.createReadStream("test.txt")); // true
```
