# JavaScript で値が非同期関数かどうかを確認する

JavaScript で値が `async` 関数かどうかを確認するには、次のコードを使用できます。

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

この関数は、`Object.prototype.toString()` と `Function.prototype.call()` を使用して、与えられた引数が `async` 関数かどうかを確認します。

通常の関数と `async` 関数を引数として渡すことで、この関数をテストできます。

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

JavaScript でコーディングを練習するには、ターミナル/SSH を開き、`node` と入力します。
