# JavaScript において文字列を空白で切り詰める方法

コーディングを練習するには、ターミナル/SSH を開き、`node` と入力します。

以下は、可能な限り空白を尊重しながら、指定された長さまで文字列を切り詰める関数です。

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

この関数を使用するには、切り詰めたい文字列を最初の引数に、最大長を 2 番目の引数に、任意のエンディング文字列を 3 番目の引数に渡します。文字列の長さが指定された制限以下の場合、元の文字列を返します。それ以外の場合、関数は制限より前の最後の空白を見つけ、そこで文字列を切り詰め、指定されている場合はエンディング文字列を追加します。

以下はいくつかの例です。

```js
truncateStringAtWhitespace("short", 10); // 'short'
truncateStringAtWhitespace("not so short", 10); // 'not so...'
truncateStringAtWhitespace("trying a thing", 10); // 'trying...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
