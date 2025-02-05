# 二分查找算法

要开始编码练习，请打开终端/SSH 并输入 `node`。二分查找算法用于在已排序的数组中找到给定元素的索引。以下是实现二分查找算法的步骤：

1. 声明左边界和右边界 `l` 和 `r`，分别初始化为 `0` 和数组的 `length`。
2. 使用 `while` 循环，通过使用 `Math.floor()` 将搜索子数组一分为二来反复缩小搜索范围。
3. 如果找到元素，则返回其索引。否则，返回 `-1`。
4. 请注意，此算法不考虑数组中的重复值。

以下是 JavaScript 中二分查找算法的示例实现：

```js
const binarySearch = (arr, item) => {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    const guess = arr[mid];
    if (guess === item) return mid;
    if (guess > item) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
};
```

你可以使用以下示例测试 `binarySearch` 函数：

```js
binarySearch([1, 2, 3, 4, 5], 1); // 0
binarySearch([1, 2, 3, 4, 5], 5); // 4
binarySearch([1, 2, 3, 4, 5], 6); // -1
```
