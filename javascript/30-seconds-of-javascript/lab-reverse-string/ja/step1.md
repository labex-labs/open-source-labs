# 文字列を逆順にする関数はこちらです：

文字列を逆順にするには、スプレッド演算子（`...`）と`Array.prototype.reverse()`を使用します。`Array.prototype.join()`を使って文字を結合して文字列を取得します。コードは次のとおりです：

```js
const reverseString = (str) => [...str].reverse().join("");
```

使用例：

```js
reverseString("foobar"); // 'raboof'
```
