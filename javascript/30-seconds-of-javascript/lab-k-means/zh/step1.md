# JavaScript 中 k 均值聚类算法的实现

要开始使用 k 均值聚类算法进行编码练习，请打开终端/SSH 并输入 `node`。此算法使用 [k 均值聚类](https://en.wikipedia.org/wiki/K-means_clustering) 算法将给定数据分组为 `k` 个聚类。

实现过程中使用了以下步骤：

1. 使用 `Array.from()` 和 `Array.prototype.slice()` 为聚类 `质心`、`距离` 和 `类别` 初始化适当的变量。
2. 使用 `while` 循环重复分配和更新步骤，只要前一次迭代中有变化，由 `itr` 指示。
3. 使用 `Math.hypot()`、`Object.keys()` 和 `Array.prototype.map()` 计算每个数据点与质心之间的欧几里得距离。
4. 使用 `Array.prototype.indexOf()` 和 `Math.min()` 找到最近的质心。
5. 使用 `Array.from()`、`Array.prototype.reduce()`、`parseFloat()` 和 `Number.prototype.toFixed()` 计算新的质心。

```js
const kMeans = (data, k = 1) => {
  const centroids = data.slice(0, k);
  const distances = Array.from({ length: data.length }, () =>
    Array.from({ length: k }, () => 0)
  );
  const classes = Array.from({ length: data.length }, () => -1);
  let itr = true;

  while (itr) {
    itr = false;

    for (let d in data) {
      for (let c = 0; c < k; c++) {
        distances[d][c] = Math.hypot(
          ...Object.keys(data[0]).map((key) => data[d][key] - centroids[c][key])
        );
      }
      const m = distances[d].indexOf(Math.min(...distances[d]));
      if (classes[d] !== m) itr = true;
      classes[d] = m;
    }

    for (let c = 0; c < k; c++) {
      centroids[c] = Array.from({ length: data[0].length }, () => 0);
      const size = data.reduce((acc, _, d) => {
        if (classes[d] === c) {
          acc++;
          for (let i in data[0]) centroids[c][i] += data[d][i];
        }
        return acc;
      }, 0);
      for (let i in data[0]) {
        centroids[c][i] = parseFloat(Number(centroids[c][i] / size).toFixed(2));
      }
    }
  }

  return classes;
};
```

要测试该算法，请使用数据数组和所需的聚类数 `k` 调用 `kMeans()` 函数。该函数返回每个数据点的类别分配数组。

```js
kMeans(
  [
    [0, 0],
    [0, 1],
    [1, 3],
    [2, 0]
  ],
  2
); // [0, 1, 1, 0]
```
