# キーと値のペアからオブジェクトを作成する

キーと値のペアからオブジェクトを作成するには、`objectFromPairs` 関数を使用します。

- ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
- この関数は、`Array.prototype.reduce()` を使用してキーと値のペアを作成して結合します。
- よりシンプルな実装には、[`Object.fromEntries()`](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries) も使用できます。

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

使用例：

```js
objectFromPairs([
  ["a", 1],
  ["b", 2]
]); // {a: 1, b: 2}
```
