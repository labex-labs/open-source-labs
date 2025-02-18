# 文字列が英数字かどうかをチェックする

コーディングの練習をしたい場合は、ターミナル/SSH を開き、`node` と入力します。以下は、文字列が英数字のみで構成されているかどうかをチェックする関数です。

```js
const isAlphaNumeric = (str) => /^[a-z0-9]+$/gi.test(str);
```

この関数を使用するには、文字列引数を指定して `isAlphaNumeric` を呼び出します。文字列が英数字のみで構成されている場合は `true` を返し、それ以外の場合は `false` を返します。

例えば：

```js
isAlphaNumeric("hello123"); // true
isAlphaNumeric("123"); // true
isAlphaNumeric("hello 123"); // false (空白文字を含む)
isAlphaNumeric("#$hello"); // false (英数字以外の文字を含む)
```

`RegExp.prototype.test()` メソッドは、入力文字列が正規表現 `/^[a-z0-9]+$/gi` で表される英数字パターンと一致するかどうかをチェックするために使用されます。このパターンは、1 つ以上の小文字または数字のシーケンスに一致し、`g` および `i` フラグにより大文字小文字を区別しない一致が行われます。
