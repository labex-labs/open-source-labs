# 检查一个值是否为 null

要在 JavaScript 中检查一个值是否为 `null`，请使用严格相等运算符 (`===`)。以下是一个示例代码片段，它定义了一个名为 `isNull` 的函数，如果给定值为 `null`，则返回 `true`，否则返回 `false`。

```js
const isNull = (val) => val === null;
```

要测试此函数，你可以将想要检查的值作为参数调用它。例如，`isNull(null)` 将返回 `true`。
