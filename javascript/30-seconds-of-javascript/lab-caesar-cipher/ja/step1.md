# シーザー暗号

シーザー暗号を使用するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. 暗号化または復号化する文字列、シフト値、および復号化するかどうかを示すブール値を使って、`caesarCipher` 関数を呼び出します。
3. `caesarCipher` 関数は、剰余演算子 (`%`) と三項演算子 (`?`) を使って、正しい暗号化または復号化キーを計算します。
4. 展開演算子 (`...`) と `Array.prototype.map()` を使って、与えられた文字列の文字を反復処理します。
5. `String.prototype.charCodeAt()` と `String.fromCharCode()` を使って、特殊文字、空白などを無視して、各文字を適切に変換します。
6. `Array.prototype.join()` を使って、すべての文字を 1 つの文字列に結合します。
7. 暗号化された文字列を復号化したい場合は、`caesarCipher` 関数を呼び出す際に、最後のパラメータである `decrypt` に `true` を渡します。

以下は、`caesarCipher` 関数のコードです。

```js
const caesarCipher = (str, shift, decrypt = false) => {
  const s = decrypt ? (26 - shift) % 26 : shift;
  const n = s > 0 ? s : 26 + (s % 26);
  return [...str]
    .map((l, i) => {
      const c = str.charCodeAt(i);
      if (c >= 65 && c <= 90)
        return String.fromCharCode(((c - 65 + n) % 26) + 65);
      if (c >= 97 && c <= 122)
        return String.fromCharCode(((c - 97 + n) % 26) + 97);
      return l;
    })
    .join("");
};
```

以下は、`caesarCipher` 関数の使用例です。

```js
caesarCipher("Hello World!", -3); // 'Ebiil Tloia!'
caesarCipher("Ebiil Tloia!", 23, true); // 'Hello World!'
```
