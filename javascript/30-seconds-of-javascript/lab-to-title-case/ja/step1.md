# 文字列をタイトルケースに変換する関数

与えられた文字列をタイトルケースに変換するには、次の関数を使用します。この関数は、適切な正規表現を使って `String.prototype.match()` を使って文字列を単語に分割します。そして、`Array.prototype.map()`、`Array.prototype.slice()`、`Array.prototype.join()`、および `String.prototype.toUpperCase()` を使ってそれらを結合します。これにより、各単語の先頭文字が大文字になり、それらの間に空白が追加されます。

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

この関数の使い方の例をいくつか示します。

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
