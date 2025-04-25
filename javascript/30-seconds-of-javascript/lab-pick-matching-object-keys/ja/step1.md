# 与えられた条件に一致するオブジェクトのキーを抽出する関数

与えられた条件に一致するオブジェクトのキーを抽出するには、`pickBy()` 関数を使用します。この関数は、与えられた関数が真を返すプロパティで構成される新しいオブジェクトを作成します。

- `Object.keys()` と `Array.prototype.filter()` を使用して、`fn` が偽を返すキーを削除します。
- `Array.prototype.reduce()` を使用して、フィルタリングされたキーを対応するキーと値のペアを持つオブジェクトに戻します。
- コールバック関数は、2 つの引数 (value, key) で呼び出されます。

以下は、`pickBy()` 関数のコードです：

```js
const pickBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});
```

この関数を使用して、条件に一致するキーを抽出できます。たとえば：

```js
pickBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number");
// { 'a': 1, 'c': 3 }
```
