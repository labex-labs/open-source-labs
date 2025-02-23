# 数値を固定小数点数表記に変換する

末尾のゼロを含まない固定小数点数表記に数値を変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Number.prototype.toFixed()` を使用して、数値を固定小数点数表記の文字列に変換します。
3. `Number.parseFloat()` を使用して、固定小数点数表記の文字列から末尾のゼロを削除して数値に戻します。
4. テンプレートリテラルを使用して、数値を文字列に変換します。

サンプルコード：

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

この関数をさまざまな入力値でテストできます。

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.5, 2); // '1.5'
```
