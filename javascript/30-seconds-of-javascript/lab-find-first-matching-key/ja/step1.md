# テストに一致する最初のキーを見つける関数

与えられたテスト関数に一致するオブジェクト内の最初のキーを見つけるには、`findKey()` 関数を使用します。まず、`Object.keys()` を使ってオブジェクトのすべてのプロパティを取得します。次に、`Array.prototype.find()` を使って各キーと値のペアにテスト関数を適用します。テスト関数は 3 つの引数を取る必要があります。値、キー、およびオブジェクトです。この関数は、テスト関数を満たす最初のキーを返します。見つからない場合は `undefined` を返します。

以下は、`findKey()` の例となる実装です。

```js
const findKey = (obj, fn) =>
  Object.keys(obj).find((key) => fn(obj[key], key, obj));
```

`findKey()` を使用するには、オブジェクトとテスト関数を引数として渡します。

```js
findKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'barney'
```

この例では、`findKey()` は `active` プロパティの値が `true` であるオブジェクト内の最初のキーである `'barney'` を返します。
