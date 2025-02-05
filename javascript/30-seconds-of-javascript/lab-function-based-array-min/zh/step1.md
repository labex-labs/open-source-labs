# 返回数组最小值的函数

要开始练习编码，请打开终端/SSH 并输入 `node`。

此函数根据提供的函数返回数组的最小值。

为此，它使用 `Array.prototype.map()` 将每个元素映射到该函数返回的值。然后使用 `Math.min()` 来获取最小值。

```js
const minBy = (arr, fn) =>
  Math.min(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

你可以通过传入一个数组和一个函数来使用此函数。例如：

```js
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 2
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 2
```
