# 如何将数组拆分成特定大小的块

要进行编码练习，请打开终端/SSH 并输入 `node`。

要将数组拆分成指定大小的较小数组，请执行以下步骤：

1. 使用 `Array.from()` 创建一个新数组，其长度与要生成的块数相匹配。
2. 使用 `Array.prototype.slice()` 将新数组的每个元素映射到一个长度为 `size` 的块。
3. 如果原始数组不能被均匀拆分，最后一个块将包含剩余的元素。

以下是一个示例代码片段：

```js
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
```

你可以通过传入要拆分的数组和所需的块大小来使用此函数。例如：

```js
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```
