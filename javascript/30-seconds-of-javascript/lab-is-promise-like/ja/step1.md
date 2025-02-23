# JavaScript Promises

オブジェクトが Promise に似ているかどうかを確認するには、`isPromiseLike` 関数を使用します。この関数は、オブジェクトが null でなく、オブジェクトまたは関数の型を持ち、`.then` プロパティも関数であるかどうかを確認します。

以下が `isPromiseLike` のコードです。

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

`isPromiseLike` を使用する方法のいくつかの例を以下に示します。

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

JavaScript でコーディングを練習するには、ターミナル/SSH を開き、`node` と入力します。
