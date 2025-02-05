# 如何在有序数组中找到插入索引

要找到将一个值插入有序数组的最低索引，请遵循以下步骤：

1. 检查数组是否按降序排序。
2. 使用 `Array.prototype.findIndex()` 方法找到应插入元素的合适索引。

以下是实现此功能的代码：

```js
const sortedIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr.findIndex((el) => (isDescending ? n >= el : n <= el));
  return index === -1 ? arr.length : index;
};
```

你可以通过传入有序数组和要插入的值来调用 `sortedIndex` 函数。以下是一些示例：

```js
sortedIndex([5, 3, 2, 1], 4); // 输出: 1
sortedIndex([30, 50], 40); // 输出: 1
```

通过使用此函数，你可以轻松找到值在有序数组中的插入索引。
