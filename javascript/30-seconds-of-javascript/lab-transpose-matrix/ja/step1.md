# JavaScript で行列を転置する

JavaScript において二次元配列を転置するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.map()` を使用して、与えられた二次元配列の転置を作成します。`map()` メソッドは、配列の各要素に対して提供された関数を呼び出した結果で新しい配列を作成します。
3. 提供された関数は 2 つの引数を取る必要があります。配列の現在の要素とそのインデックスです。この場合、転置を作成するために必要なのはインデックスだけです。
4. インデックスを使用して二次元配列の各行の対応する要素にアクセスし、それらの要素で新しい配列を作成します。これが転置された配列の新しい行になります。
5. 二次元配列の各列に対して前の手順を繰り返して、完全な転置された配列を作成します。

以下は、JavaScript で二次元配列を転置するコードです。

```js
const transpose = (arr) => arr[0].map((col, i) => arr.map((row) => row[i]));

transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]);
// [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
```
