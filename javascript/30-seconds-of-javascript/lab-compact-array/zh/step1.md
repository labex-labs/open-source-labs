# 如何使用 Array.prototype.filter() 创建精简数组

要在 JavaScript 中创建一个精简数组，你可以使用 `Array.prototype.filter()` 方法从数组中移除所有虚假值。虚假值包括 `false`、`null`、`0`、`""`、`undefined` 和 `NaN`。

以下是一个代码片段示例，展示了如何使用 `Array.prototype.filter()` 创建一个精简数组：

```js
const compact = (arr) => arr.filter(Boolean);
```

然后，你可以通过传入一个数组作为参数来使用 `compact` 函数创建一个精简数组。例如：

```js
compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]);
// 输出：[ 1, 2, 3, 'a','s', 34 ]
```

通过这种方式使用 `Array.prototype.filter()`，你可以轻松创建一个只包含真值的精简数组。
