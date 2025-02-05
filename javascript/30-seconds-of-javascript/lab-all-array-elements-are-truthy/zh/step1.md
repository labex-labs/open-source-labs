# 检查数组中的所有元素是否都为真

要检查集合中的所有元素是否都为 `true`，你可以使用 `Array.prototype.every()` 方法。此方法接受一个谓词函数作为参数，如果该函数对数组中的所有元素求值都为 `true`，则返回 `true`。

为了简化代码，你可以使用一个名为 `all` 的函数，它接受一个数组和一个可选的谓词函数作为参数。该函数使用 `Array.prototype.every()` 来检查数组中的所有元素根据提供的函数是否都返回 `true`。如果未提供函数，则默认使用 `Boolean` 函数。

以下是如何使用 `all` 函数的示例：

```js
const all = (arr, fn = Boolean) => arr.every(fn);

all([4, 2, 3], (x) => x > 1); // true
all([1, 2, 3]); // true
```
