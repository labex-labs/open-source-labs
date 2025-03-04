# 配列をオブジェクトにマッピングする

関数を使って配列の値をオブジェクトにマッピングするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Array.prototype.reduce()` を使って、`fn` を `arr` の各要素に適用し、結果をオブジェクトに結合します。
3. 各プロパティのキーとして `el` を、値として `fn` の結果を使います。

以下はコードのサンプルです。

```js
const mapObject = (arr, fn) =>
  arr.reduce((acc, el, i) => {
    acc[el] = fn(el, i, arr);
    return acc;
  }, {});
```

この例のように `mapObject` 関数を使うことができます。

```js
mapObject([1, 2, 3], (a) => a * a); // { 1: 1, 2: 4, 3: 9 }
```
