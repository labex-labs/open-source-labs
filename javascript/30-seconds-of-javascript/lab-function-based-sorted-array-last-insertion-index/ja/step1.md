# 関数に基づいてソート済み配列の最後の挿入インデックスを見つける方法

コーディングを始めるには、ターミナル/SSH を開き、`node` と入力します。

以下は、提供された反復子関数に基づいて、配列のソート順を維持するために値を挿入する最高インデックスを見つける方法です。

1. 配列が降順にソートされているかどうかを確認します。
2. `Array.prototype.map()` を使って、反復子関数を配列のすべての要素に適用します。
3. `Array.prototype.reverse()` と `Array.prototype.findIndex()` を使って、提供された反復子関数に基づいて要素を挿入する適切な最後のインデックスを見つけます。

以下のコードを参照してください。

```js
const sortedLastIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr
    .map(fn)
    .reverse()
    .findIndex((el) => (isDescending ? val <= el : val >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

以下は例です。

```js
sortedLastIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, (o) => o.x); // 1
```
