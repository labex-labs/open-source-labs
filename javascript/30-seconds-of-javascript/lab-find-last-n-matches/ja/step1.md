# 最後の N 個の一致を見つけるための指示

特定の条件に一致する最後の `n` 要素を見つけるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 以下に提供されている `findLastN` 関数を使用します。
3. 一致させたい要素に対して真値を返す配列 `arr` と `matcher` 関数を提供します。
4. 任意で、返したい一致の数 `n` も提供できます（デフォルトは 1）。
5. 関数は、最後の要素から始まる `for` ループを使用して、`arr` の各要素に対して `matcher` 関数を実行します。
6. 要素が `matcher` 条件に一致する場合、その要素は `Array.prototype.unshift()` を使用して結果配列に追加されます。これは配列の先頭に要素を追加します。
7. 結果配列の長さが `n` に等しくなると、関数は結果を返します。
8. 一致するものがない場合、または `n` が一致する数より大きい場合、空の配列が返されます。

```js
const findLastN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.unshift(el);
    if (res.length === n) return res;
  }
  return res;
};
```

以下は、`findLastN` 関数の使い方のいくつかの例です。

```js
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [4, 6]
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
