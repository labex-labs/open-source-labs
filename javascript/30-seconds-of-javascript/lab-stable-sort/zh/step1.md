# 稳定排序

要对数组进行稳定排序并保留相同值元素的初始索引，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.map()` 将输入数组的每个元素与其对应的索引配对。
3. 使用 `Array.prototype.sort()` 以及一个 `compare` 函数对列表进行排序，同时在比较的元素相等时保留初始顺序。
4. 再次使用 `Array.prototype.map()` 将数组元素转换回其初始形式。
5. 原始数组不会被修改，而是返回一个新数组。

以下是 JavaScript 中 `stableSort` 函数的实现：

```js
const stableSort = (arr, compare) =>
  arr
    .map((item, index) => ({ item, index }))
    .sort((a, b) => compare(a.item, b.item) || a.index - b.index)
    .map(({ item }) => item);
```

你可以使用一个数组和一个 `compare` 函数调用 `stableSort` 函数，以获得一个包含已排序列表的新数组，如下所示：

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const stable = stableSort(arr, () => 0); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
