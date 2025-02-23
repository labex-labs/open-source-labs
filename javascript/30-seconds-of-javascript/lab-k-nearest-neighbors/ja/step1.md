# K 近傍法（K-Nearest Neighbors Algorithm）

K 近傍法を使用するには、次の手順に従います。

1. ターミナル/SSH を開き、`node` と入力します。
2. [k 近傍法](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)を使用して、ラベル付きデータセットに対するデータポイントを分類します。
3. `Array.prototype.map()` を使用して、`data` をオブジェクトにマッピングします。各オブジェクトには、`Math.hypot()`、`Object.keys()` を使用して計算された、要素から `point` までのユークリッド距離とその `label` が含まれます。
4. `Array.prototype.sort()` と `Array.prototype.slice()` を使用して、`point` の最も近い `k` 個の近傍を取得します。
5. `Array.prototype.reduce()` を `Object.keys()` と `Array.prototype.indexOf()` と組み合わせて使用して、それらの中で最も頻繁な `label` を見つけます。

以下は、K 近傍法を実装したコードの例です。

```js
const kNearestNeighbors = (data, labels, point, k = 3) => {
  const kNearest = data
    .map((el, i) => ({
      dist: Math.hypot(...Object.keys(el).map((key) => point[key] - el[key])),
      label: labels[i]
    }))
    .sort((a, b) => a.dist - b.dist)
    .slice(0, k);

  return kNearest.reduce(
    (acc, { label }, i) => {
      acc.classCounts[label] =
        Object.keys(acc.classCounts).indexOf(label) !== -1
          ? acc.classCounts[label] + 1
          : 1;
      if (acc.classCounts[label] > acc.topClassCount) {
        acc.topClassCount = acc.classCounts[label];
        acc.topClass = label;
      }
      return acc;
    },
    {
      classCounts: {},
      topClass: kNearest[0].label,
      topClassCount: 0
    }
  ).topClass;
};
```

このコードの使い方は以下の通りです。

```js
const data = [
  [0, 0],
  [0, 1],
  [1, 3],
  [2, 0]
];
const labels = [0, 1, 1, 0];

kNearestNeighbors(data, labels, [1, 2], 2); // 1
kNearestNeighbors(data, labels, [1, 0], 2); // 0
```
