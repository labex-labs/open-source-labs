# 如何在 JavaScript 中检查一个值是否为 null 或 undefined

要在 JavaScript 中确定一个值是否为 `null` 或 `undefined`，你可以使用严格相等运算符 (`===`)。以下是一个示例代码片段，用于检查指定的值是否为 `null` 或 `undefined`：

```js
const isNil = (val) => val === undefined || val === null;
```

你可以使用这个函数来检查一个值是否为 `null` 或 `undefined`，如下所示：

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

要开始练习 JavaScript 编码，你可以打开终端/SSH 并输入 `node`。
