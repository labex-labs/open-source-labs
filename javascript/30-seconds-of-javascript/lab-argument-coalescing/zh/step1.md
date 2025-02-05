# 使用参数合并

要开始编码，请打开终端/SSH 并输入 `node`。参数合并是一种用于在参数列表中返回第一个已定义且非空参数的技术。要实现这一点，请使用 `Array.prototype.find()` 和 `Array.prototype.includes()` 来查找第一个不等于 `undefined` 或 `null` 的值。

以下是在 JavaScript 中使用参数合并的示例：

```js
const coalesce = (...args) => args.find((v) => ![undefined, null].includes(v));
```

在上面的代码片段中，`coalesce` 是一个函数，它接受任意数量的参数并返回第一个已定义且非空的参数。以下是使用 `coalesce` 函数的示例：

```js
coalesce(null, undefined, "", NaN, "Waldo"); // ''
```

在这个示例中，使用包含 `null`、`undefined`、空字符串 `''`、`NaN` 和字符串 `'Waldo'` 的参数列表调用 `coalesce`。该函数返回空字符串 `''`，因为它是列表中第一个已定义且非空的参数。
