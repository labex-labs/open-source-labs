# オブジェクトの変換

コーディングの練習を始めるには、ターミナル/SSH を開き、`node` と入力します。

`transform` 関数は、指定された関数をアキュムレータとオブジェクトの各キーに左から右へ適用します。使い方は以下の通りです。

- `Object.keys()` を使ってオブジェクトの各キーを反復処理します。
- `Array.prototype.reduce()` を使って指定された関数を与えられたアキュムレータに適用します。

```js
const transform = (obj, fn, acc) =>
  Object.keys(obj).reduce((a, k) => fn(a, obj[k], k, obj), acc);
```

以下は例です。

```js
transform(
  { a: 1, b: 2, c: 1 },
  (r, v, k) => {
    (r[v] || (r[v] = [])).push(k);
    return r;
  },
  {}
); // { '1': ['a', 'c'], '2': ['b'] }
```
