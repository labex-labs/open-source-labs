# バケットソートアルゴリズム

バケットソートアルゴリズムを使って数値の配列をソートするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Math.min()`、`Math.max()` および展開演算子 (`...`) を使って、与えられた配列の最小値と最大値を見つけます。
3. `Array.from()` と `Math.floor()` を使って、適切な数の `バケット`（空の配列）を作成します。
4. `Array.prototype.forEach()` を使って、配列から適切な要素を各バケットに格納します。
5. `Array.prototype.reduce()`、展開演算子 (`...`) および `Array.prototype.sort()` を使って、各バケットをソートして結果に追加します。

次に、JavaScript でのバケットソートアルゴリズムの例の実装を示します。

```js
const bucketSort = (arr, size = 5) => {
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const buckets = Array.from(
    { length: Math.floor((max - min) / size) + 1 },
    () => []
  );
  arr.forEach((val) => {
    buckets[Math.floor((val - min) / size)].push(val);
  });
  return buckets.reduce((acc, b) => [...acc, ...b.sort((a, b) => a - b)], []);
};
```

アルゴリズムをテストするには、次のコードを実行します。

```js
bucketSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
