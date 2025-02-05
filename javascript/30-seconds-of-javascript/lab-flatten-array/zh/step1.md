# 如何使用 JavaScript 扁平化数组

要在 JavaScript 中将数组扁平化至指定深度，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `flatten` 函数，该函数带有两个参数：`arr`（要扁平化的数组）和 `depth`（要扁平化的最大嵌套层数）。
3. 在 `flatten` 函数内部，使用递归为每个深度级别将 `depth` 减 `1`。
4. 使用 `Array.prototype.reduce()` 和 `Array.prototype.concat()` 来合并元素或数组。
5. 当 `depth` 等于 `1` 时添加一个基础情况以停止递归。
6. 省略第二个参数 `depth` 以仅扁平化到深度 `1`（单次扁平化）。

以下是 `flatten` 函数的代码：

```js
const flatten = (arr, depth = 1) =>
  arr.reduce(
    (a, v) =>
      a.concat(depth > 1 && Array.isArray(v) ? flatten(v, depth - 1) : v),
    []
  );
```

你可以使用以下示例测试 `flatten` 函数：

```js
flatten([1, [2], 3, 4]); // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2); // [1, 2, 3, [4, 5], 6, 7, 8]
```
