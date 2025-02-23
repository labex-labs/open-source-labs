# オブジェクトのキーをマッピングする関数

与えられた関数を使ってオブジェクトのキーをマッピングし、新しいオブジェクトを生成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Object.keys()` を使ってオブジェクトのキーを反復処理します。
3. `Array.prototype.reduce()` を使って、与えられた関数 (`fn`) を使って同じ値とマッピングされたキーを持つ新しいオブジェクトを作成します。

以下は、`mapKeys` 関数の例の実装です。

```js
const mapKeys = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[fn(obj[k], k, obj)] = obj[k];
    return acc;
  }, {});
```

この関数を次のような例の入力でテストすることができます。

```js
mapKeys({ a: 1, b: 2 }, (val, key) => key + val); // { a1: 1, b2: 2 }
```
