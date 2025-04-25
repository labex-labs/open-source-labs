# 如何在 JavaScript 中找到性能最佳的函数

要在 JavaScript 中找到性能最佳的函数，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.map()` 生成一个数组，其中每个值是函数执行 `iterations` 次后的总执行时间。
3. 使用 `performance.now()` 值前后的差值，以高精度获取以毫秒为单位的总时间。
4. 使用 `Math.min()` 找到最短执行时间，并返回该最短时间对应的索引，该索引对应于性能最佳的函数的索引。
5. 如果你省略第二个参数 `iterations`，则函数将使用默认的 `10000` 次迭代。
6. 请记住，使用的迭代次数越多，结果就越可靠，但所需时间也越长。

以下是一个示例代码片段：

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

要使用此函数，请将函数数组作为第一个参数，并将迭代次数作为第二个参数（可选）传递。例如：

```js
mostPerformant([
  () => {
    // 在返回 `false` 之前遍历整个数组
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // 在返回 `false` 之前只需要到达索引 `1`
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
