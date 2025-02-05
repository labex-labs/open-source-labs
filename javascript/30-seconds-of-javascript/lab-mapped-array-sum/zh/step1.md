# 计算映射数组元素总和的函数

要通过使用提供的函数将数组中的每个元素映射到一个值来计算数组的总和，请使用 `sumBy` 函数。此函数使用 `Array.prototype.map()` 将每个元素映射到 `fn` 返回的值。然后，它使用 `Array.prototype.reduce()` 将每个值添加到累加器中，累加器初始值为 `0`。

```js
const sumBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0);
```

示例用法：

```js
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 返回 20
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 返回 20
```

要开始使用此函数进行编码练习，请打开终端/SSH 并输入 `node`。
