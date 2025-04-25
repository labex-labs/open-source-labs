# コールバック関数に基づくオブジェクトのキーの削除

コールバック関数に基づいてオブジェクトのキーを削除するには、`omitBy` 関数を使用します。

- `omitBy` は、与えられた関数に対して偽を返すプロパティで構成されるオブジェクトを作成します。
- `Object.keys()` と `Array.prototype.filter()` は、`fn` が真を返すキーを削除するために使用されます。
- `Array.prototype.reduce()` は、フィルタリングされたキーを対応するキーと値のペアを持つオブジェクトに戻します。
- コールバック関数には 2 つの引数があります。`value` と `key`。
- 以下の例は、`omitBy` を使用してオブジェクトから数値型のキーを削除する方法を示しています。

```js
const omitBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => !fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});

omitBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number"); // { b: '2' }
```
