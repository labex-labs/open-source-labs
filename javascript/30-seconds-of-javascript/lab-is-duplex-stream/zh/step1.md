# 检查流是否为双工流

要检查一个流是否为双工流（可读且可写），请打开终端/SSH并输入`node`以开始练习编码。然后，按照以下步骤操作：

1. 检查给定的参数是否不等于`null`。
2. 使用`typeof`检查给定的参数是否为`object`类型，并且它是否具有类型为`function`的`pipe`属性。
3. 此外，检查`_read`、`_write`、`_readableState`和`_writableState`属性是否分别为`function`和`object`类型。

以下是代码：

```js
const isDuplexStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

你可以使用以下示例测试此代码：

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
