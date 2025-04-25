# JavaScript で配列をフラット化する方法

JavaScript で配列を指定された深さまでフラット化するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `flatten` 関数に 2 つの引数を使用します。`arr`（フラット化する配列）と `depth`（フラット化するネストレベルの最大数）。
3. `flatten` 関数の中で、再帰を使って深さの各レベルで `depth` を 1 減らします。
4. `Array.prototype.reduce()` と `Array.prototype.concat()` を使って要素や配列をマージします。
5. `depth` が 1 に等しい場合のベースケースを追加して再帰を停止します。
6. 2 番目の引数 `depth` を省略すると、深さ 1 までのみフラット化されます（単一のフラット化）。

以下が `flatten` 関数のコードです。

```js
const flatten = (arr, depth = 1) =>
  arr.reduce(
    (a, v) =>
      a.concat(depth > 1 && Array.isArray(v) ? flatten(v, depth - 1) : v),
    []
  );
```

次の例で `flatten` 関数をテストできます。

```js
flatten([1, [2], 3, 4]); // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2); // [1, 2, 3, [4, 5], 6, 7, 8]
```
