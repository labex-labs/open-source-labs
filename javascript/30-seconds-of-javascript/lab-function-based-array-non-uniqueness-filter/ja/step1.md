# 関数を使った非一意の配列値のフィルタリング

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。

このコードは、提供された比較関数に基づいて配列から非一意の値をフィルタリングします。これを達成する手順は以下の通りです。

1. `Array.prototype.filter()` と `Array.prototype.every()` を使用して、比較関数 `fn` に基づいて一意の値のみを含む新しい配列を作成します。
2. 比較関数には 4 つの引数が渡されます。比較される 2 つの要素の値とそれらのインデックスです。
3. `filterNonUniqueBy` 関数は上記の手順を実装し、一意の値の配列を返します。

```js
const filterNonUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.every((x, j) => (i === j) === fn(v, x, i, j)));
```

この関数の使い方の例を以下に示します。

```js
filterNonUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id === b.id
); // [ { id: 2, value: 'c' } ]
```

このコードは簡潔で、明確で一貫性があり、期待通りに動作するはずです。
