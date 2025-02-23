# ソート済み配列における最後の挿入インデックスの説明

配列のソート順を維持するために値を挿入する最高のインデックスを見つけるには、次の手順に従います。

- まず、配列が降順にソートされているかどうかを緩やかに確認します。
- 次に、`Array.prototype.reverse()` と `Array.prototype.findIndex()` を使用して、要素を挿入する適切な最後のインデックスを見つけます。

ここに関数のコードがあります。

```js
const sortedLastIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr
    .reverse()
    .findIndex((el) => (isDescending ? n <= el : n >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

そして、この関数を使用する方法の例があります。

```js
sortedLastIndex([10, 20, 30, 30, 40], 30); // 4
```

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。
