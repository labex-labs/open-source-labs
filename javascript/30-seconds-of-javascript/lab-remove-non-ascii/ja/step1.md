# JavaScript で非 ASCII 文字を削除する方法

JavaScript で非表示可能な ASCII 文字を削除するには、以下の手順に従ってください。

1. ターミナル/SSH を開き、`node` と入力してコーディングの練習を開始します。
2. 正規表現を使用して `String.prototype.replace()` メソッドを使い、非表示可能な ASCII 文字を削除します。
3. 正規表現 `/[^\x20-\x7E]/g` は、表示可能な ASCII 範囲（10 進数で 32 から 126）に含まれない任意の文字に一致します。
4. `g` フラグは、グローバルマッチを行うために使用されます（つまり、文字列内のすべての非 ASCII 文字の出現箇所を置き換えます）。
5. `removeNonASCII` 関数の使用例を次に示します。

```js
const removeNonASCII = (str) => str.replace(/[^\x20-\x7E]/g, "");

removeNonASCII("äÄçÇéÉêlorem-ipsumöÖÐþúÚ"); // 'lorem-ipsum'
```

これにより、すべての非 ASCII 文字が削除された文字列が返されます。
