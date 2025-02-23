# 配列を分割するアルゴリズム

配列を分割するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 与えられた配列 `arr` の各値に対して、提供された関数 `fn` を適用します。
3. `fn` が新しい値を返すたびに、配列を分割します。
4. `Array.prototype.reduce()` を使用して、結果の配列と `fn` から返された最後の値を保持する累積オブジェクトを作成します。
5. `Array.prototype.push()` を使用して、`arr` の各値を累積配列の適切なパーティションに追加します。
6. 結果の配列を返します。

以下はコードの実装です。

```js
const partitionBy = (arr, fn) =>
  arr.reduce(
    ({ res, last }, v, i, a) => {
      const next = fn(v, i, a);
      if (next !== last) res.push([v]);
      else res[res.length - 1].push(v);
      return { res, last: next };
    },
    { res: [] }
  ).res;
```

使用例:

```js
const numbers = [1, 1, 3, 3, 4, 5, 5, 5];
partitionBy(numbers, (n) => n % 2 === 0); // [[1, 1, 3, 3], [4], [5, 5, 5]]
partitionBy(numbers, (n) => n); // [[1, 1], [3, 3], [4], [5, 5, 5]]
```
