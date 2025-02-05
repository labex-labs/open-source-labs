# 使用给定函数检查数组元素是否相等

要检查数组中的所有元素是否相等，请使用 `allEqualBy` 函数。此函数将给定的映射函数 `fn` 应用于数组 `arr` 的第一个元素。然后，它使用 `Array.prototype.every()` 检查 `fn` 对数组中所有元素返回的值是否与对第一个元素返回的值相同。该函数使用严格比较运算符，不考虑 `NaN` 的自身不相等性。

以下是 `allEqualBy` 的代码：

```js
const allEqualBy = (arr, fn) => {
  const eql = fn(arr[0]);
  return arr.every((val) => fn(val) === eql);
};
```

你可以这样使用 `allEqualBy`：

```js
allEqualBy([1.1, 1.2, 1.3], Math.round); // true
allEqualBy([1.1, 1.3, 1.6], Math.round); // false
```

要开始使用此函数进行编码练习，请打开终端/SSH 并输入 `node`。
