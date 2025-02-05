# 用于检查一个数组是否包含所有值的函数

如果你想检查数组 `values` 中的所有元素是否都包含在另一个数组 `arr` 中，可以使用 JavaScript 中的 `includesAll` 函数。

要开始使用该函数，请打开终端/SSH 并输入 `node`。

以下是 `includesAll` 函数的工作原理：

- 它使用 `Array.prototype.every()` 和 `Array.prototype.includes()` 方法来检查 `values` 中的所有元素是否都包含在 `arr` 中。
- 如果 `values` 中的所有元素都包含在 `arr` 中，该函数将返回 `true`。否则，它将返回 `false`。

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

以下是如何使用 `includesAll` 函数的示例：

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
