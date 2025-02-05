# 如何基于一个函数在有序数组中找到最后插入索引

要开始编码，请打开终端/SSH 并输入 `node`。

以下是如何根据提供的迭代器函数找到为了保持数组的排序顺序，一个值应该插入到数组中的最高索引：

1. 检查数组是否按降序排序。
2. 使用 `Array.prototype.map()` 将迭代器函数应用于数组的所有元素。
3. 使用 `Array.prototype.reverse()` 和 `Array.prototype.findIndex()` 根据提供的迭代器函数找到元素应该插入的合适最后索引。

请查看以下代码：

```js
const sortedLastIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr
    .map(fn)
    .reverse()
    .findIndex((el) => (isDescending ? val <= el : val >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

以下是一个示例：

```js
sortedLastIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, (o) => o.x); // 1
```
