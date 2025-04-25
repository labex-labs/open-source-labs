# 配列の順位付け

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。この関数は、比較関数に基づいて配列の順位を計算します。

この関数を使用するには、次のようにできます。

- `Array.prototype.map()` と `Array.prototype.filter()` を使用して、提供された比較関数を使って各要素を順位にマッピングします。

以下は使用例です。

```js
const ranking = (arr, compFn) =>
  arr.map((a) => arr.filter((b) => compFn(a, b)).length + 1);
```

例：

```js
ranking([8, 6, 9, 5], (a, b) => a < b);
// [2, 3, 1, 4]
ranking(["c", "a", "b", "d"], (a, b) => a.localeCompare(b) > 0);
// [3, 1, 2, 4]
```
