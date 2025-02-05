# 如何计算数字数组的中位数

要计算数字数组的中位数，请遵循以下步骤：

1. 找到数组的中间位置。
2. 使用 `Array.prototype.sort()` 对值进行排序。
3. 如果 `Array.prototype.length` 是奇数，则返回中间位置的数字。如果是偶数，则返回中间两个数字的平均值。
4. 要开始练习编码并使用 `node`，请打开终端/SSH 并输入 `node`。

以下是一个实现此逻辑的示例代码片段：

```js
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = [...arr].sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};
```

你可以使用数字数组调用此函数，如下所示：

```js
median([5, 6, 50, 1, -5]); // 5
```
