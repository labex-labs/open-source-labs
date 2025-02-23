# JavaScript における挿入ソートアルゴリズム

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。このアルゴリズムは挿入ソート法を使って数値の配列をソートします。このアルゴリズムを実装するには、次の手順に従ってください。

1. `Array.prototype.reduce()` を使って、与えられた配列のすべての要素を反復処理します。
2. アキュムレータの `length` が `0` の場合、現在の要素を追加します。
3. `Array.prototype.some()` を使って、アキュムレータの結果を反復処理して、正しい位置が見つかるまで続けます。
4. `Array.prototype.splice()` を使って、現在の要素をアキュムレータに挿入します。

以下は、JavaScript で挿入ソートを実装するコードです。

```js
const insertionSort = (arr) =>
  arr.reduce((acc, x) => {
    if (!acc.length) return [x];
    acc.some((y, j) => {
      if (x <= y) {
        acc.splice(j, 0, x);
        return true;
      }
      if (x > y && j === acc.length - 1) {
        acc.splice(j + 1, 0, x);
        return true;
      }
      return false;
    });
    return acc;
  }, []);
```

次のコードでアルゴリズムをテストできます。

```js
insertionSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
