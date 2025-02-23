# コード演習：配列がソートされているかどうかを確認する

コーディングの練習のために、ターミナル/SSH を開き、`node` と入力します。

ここに、数値配列がソートされているかどうかを確認する関数があります。

```js
const isSorted = (arr) => {
  if (arr.length <= 1) return 0;
  const direction = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if ((arr[i] - arr[i - 1]) * direction < 0) return 0;
  }
  return Math.sign(direction);
};
```

これを使用するには、数値の配列を `isSorted()` に渡します。配列が昇順にソートされている場合は関数は `1` を返し、降順にソートされている場合は `-1` を返し、ソートされていない場合は `0` を返します。

以下はいくつかの例です。

```js
isSorted([0, 1, 2, 2]); // 1
isSorted([4, 3, 2]); // -1
isSorted([4, 3, 5]); // 0
isSorted([4]); // 0
```
