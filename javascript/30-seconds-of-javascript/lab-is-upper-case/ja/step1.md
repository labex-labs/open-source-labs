# 文字列を大文字かどうかをチェックする関数

文字列を大文字かどうかをチェックするには、次の手順に従います。

1. ターミナル/SSH を開きます。
2. `node` と入力します。
3. `String.prototype.toUpperCase()` を使って与えられた文字列を大文字に変換し、元の文字列と比較するために `isUpperCase()` 関数を使います。
4. 文字列が大文字の場合は関数は `true` を返し、そうでない場合は `false` を返します。

以下はコードの例です。

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
