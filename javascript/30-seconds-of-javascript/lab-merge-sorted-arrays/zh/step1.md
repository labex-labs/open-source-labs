# 用 JavaScript 合并已排序数组的说明

要在 JavaScript 中合并两个已排序的数组，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用展开运算符（`...`）克隆给定的两个数组。
3. 使用 `Array.from()` 根据给定数组创建一个长度合适的数组。
4. 使用 `Array.prototype.shift()` 从克隆数组中移除的元素填充新创建的数组。

以下是合并两个已排序数组的示例代码片段：

```js
const mergeSortedArrays = (a, b) => {
  const _a = [...a],
    _b = [...b];
  return Array.from({ length: _a.length + _b.length }, () => {
    if (!_a.length) return _b.shift();
    else if (!_b.length) return _a.shift();
    else return _a[0] > _b[0] ? _b.shift() : _a.shift();
  });
};

console.log(mergeSortedArrays([1, 4, 5], [2, 3, 6])); // 输出: [1, 2, 3, 4, 5, 6]
```

在上述代码中，`mergeSortedArrays` 函数接受两个已排序数组作为参数，并按照上述步骤返回合并后的数组。示例代码的输出是 `[1, 2, 3, 4, 5, 6]`。
