# 斐波那契数列

要在 JavaScript 中生成斐波那契数列，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node`。
2. 使用 `Array.from()` 创建一个特定长度的空数组，并初始化前两个值（`0` 和 `1`）。
3. 使用 `Array.prototype.reduce()` 和 `Array.prototype.concat()` 将值添加到数组中，除了前两个值外，使用最后两个值的和。
4. 调用 `fibonacci()` 函数，并将所需的数列长度作为参数传递。

以下是代码：

```js
const fibonacci = (n) =>
  Array.from({ length: n }).reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  );

fibonacci(6); // [0, 1, 1, 2, 3, 5]
```

这将生成一个包含第 n 项之前的斐波那契数列的数组。
