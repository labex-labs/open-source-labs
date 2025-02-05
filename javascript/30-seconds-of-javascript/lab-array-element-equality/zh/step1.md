# 检查数组元素是否相等

要检查数组中的所有元素是否相同，可以使用 `Array.prototype.every()` 方法，该方法会将所有元素与第一个元素进行比较。

以下是实现方法：

```js
const allEqual = (arr) => arr.every((val) => val === arr[0]);
```

请注意，这里使用了 `严格相等比较` 运算符来比较元素。此运算符不考虑 `NaN` 的自身不相等情况。

示例用法：

```js
allEqual([1, 2, 3, 4, 5, 6]); // false
allEqual([1, 1, 1, 1]); // true
```
