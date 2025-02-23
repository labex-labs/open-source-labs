# 数値を逆順にする

JavaScript を使って数値を逆順にするには、次の手順で `reverseNumber()` 関数を使用できます。

1. `Object.prototype.toString()` を使って数値 `n` を文字列に変換します。
2. `String.prototype.split()`、`Array.prototype.reverse()`、`Array.prototype.join()` を使って、`n` の逆順の値を文字列として取得します。
3. `parseFloat()` を使って文字列を再度数値に変換します。
4. `Math.sign()` を使って数値の符号を維持します。

以下が `reverseNumber()` 関数のコードです。

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

この関数を以下の例でテストできます。

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
