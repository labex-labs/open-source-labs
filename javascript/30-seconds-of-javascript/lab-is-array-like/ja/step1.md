# 値が配列のようなものかどうかを確認する

値が配列のようなものかどうかを確認するには、次の手順に従います。

1. ターミナル/SSH を開きます。
2. `node` を入力します。
3. 次のコードを使用して、提供された引数が反復可能かどうかを確認します。

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. 関数は、提供された引数が配列のようなオブジェクトの場合に `true` を返し、それ以外の場合は `false` を返します。
5. たとえば：

```js
isArrayLike([1, 2, 3]); // true
isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
