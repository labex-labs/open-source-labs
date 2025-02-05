# 查找连续元素的数组

要查找连续元素的数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.slice()` 创建一个从开头移除了 `n - 1` 个元素的数组。
3. 使用 `Array.prototype.map()` 和 `Array.prototype.slice()` 将每个元素映射为一个包含 `n` 个连续元素的数组。

以下是一个实现这些步骤的示例函数：

```js
const findConsecutive = (arr, n) =>
  arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

你可以使用一个数组和数字 `n` 调用此函数，以查找数组中所有包含 `n` 个连续元素的数组。例如：

```js
findConsecutive([1, 2, 3, 4, 5], 2);
// [[1, 2], [2, 3], [3, 4], [4, 5]]
```
