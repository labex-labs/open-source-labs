# 最初の N 個の一致する要素を見つける方法

特定の基準を満たす最初の `n` 要素を見つけるには、`findFirstN` 関数を使用します。方法は次のとおりです。

1. ターミナル/SSH を開きます。
2. コーディングを練習するには `node` と入力します。
3. 探索対象の配列、一致関数、および見つける一致数（指定しない場合はデフォルトは 1）を渡して `findFirstN` 関数を使用します。
4. `matcher` 関数は `arr` の各要素に対して実行され、真値を返す場合、その要素が結果配列に追加されます。
5. `res` 配列の長さが `n` に達すると、関数は結果配列を返します。
6. 一致するものが見つからない場合は、空の配列が返されます。

ここに `findFirstN` 関数のコードを示します。

```js
const findFirstN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i in arr) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.push(el);
    if (res.length === n) return res;
  }
  return res;
};
```

そして、それを使用する方法のいくつかの例を示します。

```js
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [2, 4]
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
