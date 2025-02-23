# JavaScript で文字列を切り詰める

JavaScript で文字列を切り詰めるには、`truncateString` 関数を使用できます。この関数には 2 つの引数が必要です。`str`（切り詰める文字列）と `num`（切り詰められた文字列の最大長）です。

`truncateString` 関数は、`str` の長さが `num` より大きいかどうかを確認します。もしそうなら、関数は文字列を望ましい長さに切り詰めて末尾に `'...'` を追加します。そうでなければ、元の文字列を返します。

以下は `truncateString` 関数のコードです。

```js
const truncateString = (str, num) =>
  str.length > num ? str.slice(0, num > 3 ? num - 3 : num) + "..." : str;
```

そして、`truncateString` 関数を使用する方法の例を以下に示します。

```js
truncateString("boomerang", 7); // 'boom...'
```
