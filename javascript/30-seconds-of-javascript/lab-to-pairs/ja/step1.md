# オブジェクトをペアに変換する

オブジェクトをキーと値のペアの配列に変換するには、`toPairs`関数を使用します。コーディングを始めるには、ターミナル/SSH を開き、`node`と入力します。

`toPairs`関数は以下のように機能します。

- まず、与えられた反復可能オブジェクトに対して`Symbol.iterator`が定義されているかどうかを確認します。
- `Symbol.iterator`が定義されている場合、`Array.prototype.entries()`を使用してオブジェクトの反復子を取得し、その結果を`Array.from()`を使用してキーと値のペアの配列に変換します。
- オブジェクトに`Symbol.iterator`が定義されていない場合、代わりに`Object.entries()`を使用します。

以下は`toPairs`関数のコードです。

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

`toPairs`関数は、次のようなさまざまな種類のオブジェクトで使用できます。

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0','s'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
