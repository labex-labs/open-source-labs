# 如何将一个数组拆分成 N 个块

要将一个数组拆分成 `n` 个较小的数组，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Math.ceil()` 和 `Array.prototype.length` 来计算每个块的大小。
3. 使用 `Array.from()` 创建一个大小为 `n` 的新数组。
4. 使用 `Array.prototype.slice()` 将新数组的每个元素映射到一个长度为 `size` 的块。
5. 如果原始数组不能被均匀拆分，最后一个块将包含剩余的元素。

以下是 JavaScript 中 `chunkIntoN` 函数的一个示例实现：

```js
const chunkIntoN = (arr, n) => {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
};
```

你可以通过将数组和所需的块数作为参数传递来使用此函数将一个数组拆分成 `n` 个块。例如：

```js
chunkIntoN([1, 2, 3, 4, 5, 6, 7], 4); // [[1, 2], [3, 4], [5, 6], [7]]
```
