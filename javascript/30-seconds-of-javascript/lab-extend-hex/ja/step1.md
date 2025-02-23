# 3桁のカラーコードを6桁のカラーコードに拡張する方法

コーディングを練習するには、ターミナル/SSHを開いて `node` と入力します。3桁のカラーコードを6桁のカラーコードに拡張するには、次の関数を使用できます。

```js
const extendHex = (shortHex) =>
  "#" +
  shortHex
    .slice(shortHex.startsWith("#") ? 1 : 0)
    .split("")
    .map((x) => x + x)
    .join("");
```

3桁のRGB表記の16進数カラーコードを6桁の形式に変換するには、次の手順に従います。

- `Array.prototype.map()`、`String.prototype.split()`、および `Array.prototype.join()` を使用して、マッピングされた配列を結合します。
- 一度追加されるため、文字列の先頭から `#` を削除するには、`Array.prototype.slice()` を使用します。

以下はいくつかの例です。

```js
extendHex("#03f"); // '#0033ff'
extendHex("05a"); // '#0055aa'
```
