# 文字列を改行するための指示

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。

このコードは、文字列を特定の文字数に改行文字を使って改行します。それを使用するには、次の手順に従います。

1. `String.prototype.replace()` と正規表現を使って、`max` 文字の最も近い空白の場所に指定された改行文字を挿入します。
2. 3番目の引数 `br` に対して `'\n'` のデフォルト値を使用したくない場合は、それを省略して独自の文字を指定できます。

コードは次のとおりです。

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

そして、それを使用する方法のいくつかの例は次のとおりです。

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
