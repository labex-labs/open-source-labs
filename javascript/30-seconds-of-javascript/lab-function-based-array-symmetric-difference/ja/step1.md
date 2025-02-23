# 配列の対称差を見つける関数

比較関数として与えられた関数を使って2つの配列の対称差を見つけるには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。
2. `Array.prototype.filter()` と `Array.prototype.findIndex()` メソッドを使って適切な値を見つけます。
3. 与えられたコードを使って操作を実行します。

```js
const symmetricDifferenceWith = (arr, val, comp) => [
  ...arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1),
  ...val.filter((a) => arr.findIndex((b) => comp(a, b)) === -1)
];
```

たとえば、次の入力を考えてみましょう。

```js
symmetricDifferenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
); // [1, 1.2, 3.9]
```

上記のコードは、2つの配列の対称差として `[1, 1.2, 3.9]` を返します。
