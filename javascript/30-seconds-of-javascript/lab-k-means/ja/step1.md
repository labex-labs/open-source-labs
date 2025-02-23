# JavaScript における k-means クラスタリングアルゴリズムの実装

k-means クラスタリングアルゴリズムを使ってコーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。このアルゴリズムは、[k-means クラスタリング](https://en.wikipedia.org/wiki/K-means_clustering)アルゴリズムを使って、与えられたデータを `k` 個のクラスタにグループ化します。

実装には次の手順が使われます。

1. `Array.from()` と `Array.prototype.slice()` を使って、クラスタの「重心」`centroids`、「距離」`distances`、「クラス」`classes` 用の適切な変数を初期化します。
2. 前の反復での変更が `itr` によって示される限り、`while` ループを使って割り当てと更新の手順を繰り返します。
3. `Math.hypot()`、`Object.keys()`、`Array.prototype.map()` を使って、各データポイントと重心の間のユークリッド距離を計算します。
4. `Array.prototype.indexOf()` と `Math.min()` を使って最も近い重心を見つけます。
5. `Array.from()`、`Array.prototype.reduce()`、`parseFloat()`、`Number.prototype.toFixed()` を使って新しい重心を計算します。

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

アルゴリズムをテストするには、データ配列と望ましいクラスタ数 `k` を使って `kMeans()` 関数を呼び出します。この関数は、各データポイントのクラス割り当ての配列を返します。

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
