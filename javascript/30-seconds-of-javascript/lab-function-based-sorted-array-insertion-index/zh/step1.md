# 在有序数组中查找插入索引的函数

要在数组中找到插入某个值并保持其排序顺序的最低索引，可以在 JavaScript 中使用函数 `sortedIndexBy(arr, n, fn)`。

此函数会大致检查数组是否按降序排序，然后使用 `Array.prototype.findIndex()` 根据迭代器函数 `fn` 找到合适的索引。

以下是 `sortedIndexBy()` 函数的代码：

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

你可以使用一个对象数组、要插入的值和一个迭代器函数来调用这个函数。

例如，`sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)` 返回 `0`，这是 `{ x: 4 }` 对象为了基于 `x` 属性保持排序顺序而应该插入的索引。
