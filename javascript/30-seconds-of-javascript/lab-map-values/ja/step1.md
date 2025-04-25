# オブジェクトの値をマッピングする関数

与えられた関数を使ってオブジェクトの値をマッピングし、同じキーを持つ新しいオブジェクトを生成するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Object.keys()` を使ってオブジェクトのキーを反復処理します。
3. `Array.prototype.reduce()` を使って、与えられた関数 `fn` を使って同じキーとマッピングされた値を持つ新しいオブジェクトを作成します。
4. 以下のコードは、`mapValues` 関数の実装を示しています。

```js
const mapValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k] = fn(obj[k], k, obj);
    return acc;
  }, {});
```

ここに `mapValues` 関数の使用例があります。

```js
const users = {
  fred: { user: "fred", age: 40 },
  pebbles: { user: "pebbles", age: 1 }
};
mapValues(users, (u) => u.age); // { fred: 40, pebbles: 1 }
```
