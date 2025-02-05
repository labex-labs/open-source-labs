# 在 JavaScript 中创建数组的叉积

要在 JavaScript 中创建数组的叉积，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.reduce()`、`Array.prototype.map()` 和 `Array.prototype.concat()` 从两个数组的元素中生成每一个可能的对。
3. 函数 `xProd()` 接受两个数组作为参数，并通过从数组中创建每一个可能的对，基于这两个给定的数组创建一个新数组。
4. 以下是 `xProd()` 函数的一个实际示例：

```js
const xProd = (a, b) =>
  a.reduce((acc, x) => acc.concat(b.map((y) => [x, y])), []);

xProd([1, 2], ["a", "b"]); // [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
```

这将返回一个包含两个输入数组中所有可能元素对的数组。
