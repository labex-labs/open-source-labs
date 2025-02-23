# 文字列内の空白を圧縮する関数

文字列内の空白を圧縮するには、`compactWhitespace()` 関数を使用します。

- `String.prototype.replace()` を正規表現とともに使用して、2つ以上の空白文字のすべての出現箇所を1つの空白に置き換えます。
- この関数は文字列引数を取り、圧縮された文字列を返します。

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

使用例：

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
