# JavaScript で文字列を大文字と小文字を入れ替える方法

JavaScript で文字列を大文字と小文字を入れ替えるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために`node`と入力します。
2. スプレッド演算子（`...`）を使用して、入力文字列`str`を文字の配列に変換します。
3. `String.prototype.toLowerCase()`と`String.prototype.toUpperCase()`を使用して、小文字の文字を大文字に変換し、その逆も行います。
4. `Array.prototype.map()`を使用して各文字に変換を適用し、`Array.prototype.join()`を使用して文字を再び文字列に結合します。
5. 文字列の大文字と小文字を 2 回入れ替えると必ずしも元の文字列になるとは限らないことに注意してください。

以下は、JavaScript で文字列を大文字と小文字を入れ替える方法を示すコードの例です。

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // 出力：'hELLO WORLD!'
```
