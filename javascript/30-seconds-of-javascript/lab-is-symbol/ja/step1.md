# JavaScript で値がシンボルかどうかを確認する

JavaScript で値がシンボルのプリミティブであるかどうかを確認するには、`typeof` 演算子を使用できます。次に、使用できるコード スニペットの例を示します。

```js
const isSymbol = (val) => typeof val === "symbol";
```

`isSymbol` 関数を呼び出して、シンボルを引数として渡して、それが `true` を返すかどうかを確認できます。次に例を示します。

```js
isSymbol(Symbol("x")); // true
```
