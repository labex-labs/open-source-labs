# 与えられた関数を使って配列要素が等しいかどうかを確認する

配列のすべての要素が等しいかどうかを確認するには、`allEqualBy` 関数を使います。この関数は、与えられたマッピング関数 `fn` を配列 `arr` の最初の要素に適用します。その後、`Array.prototype.every()` を使って、配列のすべての要素に対して `fn` が最初の要素に対して返したものと同じ値を返すかどうかを確認します。この関数は、厳密な比較演算子を使っており、`NaN` 自身の不等性を考慮していません。

以下は `allEqualBy` のコードです。

```js
const allEqualBy = (arr, fn) => {
  const eql = fn(arr[0]);
  return arr.every((val) => fn(val) === eql);
};
```

このようにして `allEqualBy` を使うことができます。

```js
allEqualBy([1.1, 1.2, 1.3], Math.round); // true
allEqualBy([1.1, 1.3, 1.6], Math.round); // false
```

この関数を使ってコーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。
