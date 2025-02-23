# マージソートアルゴリズム

マージソートアルゴリズムを使ったコーディングを練習するには、次の手順に従います。

1. ターミナル/SSH を開き、`node` と入力します。
2. 再帰を使って数字の配列をソートします。
3. 配列の `length` が `2` 未満の場合、配列を返します。
4. `Math.floor()` を使って配列の中央点を計算します。
5. `Array.prototype.slice()` を使って配列を 2 つに分割し、生成されたサブ配列に対して再帰的に `mergeSort()` を呼び出します。
6. 最後に、`Array.from()` と `Array.prototype.shift()` を使って 2 つのソート済みサブ配列を 1 つに結合します。

以下がコードです。

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

この例で試してみましょう。

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
