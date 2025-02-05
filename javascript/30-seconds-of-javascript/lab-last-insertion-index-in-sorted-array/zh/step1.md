# 有序数组中最后插入索引的说明

要找到为了保持数组排序顺序，某个值应插入的最高索引，请遵循以下步骤：

- 首先，大致检查数组是否按降序排序。
- 然后，使用 `Array.prototype.reverse()` 和 `Array.prototype.findIndex()` 来找到元素应插入的合适最后索引。

以下是该函数的代码：

```js
const sortedLastIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr
    .reverse()
    .findIndex((el) => (isDescending ? n <= el : n >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

以下是使用该函数的示例：

```js
sortedLastIndex([10, 20, 30, 30, 40], 30); // 4
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
