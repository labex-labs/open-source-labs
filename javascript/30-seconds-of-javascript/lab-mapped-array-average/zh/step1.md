# 计算映射数组平均值的说明

要计算数组的平均值，你可以使用提供的函数将每个元素映射到一个新值。以下是步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.map()` 将每个元素映射到 `fn` 返回的值。
3. 使用 `Array.prototype.reduce()` 将每个映射后的值添加到初始值为 `0` 的累加器中。
4. 将结果数组除以其长度以得到平均值。

以下是你可以使用的代码：

```js
const averageBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0) / arr.length;
```

你可以使用以下示例测试此函数：

```js
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (o) => o.n); // 5
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 5
```
