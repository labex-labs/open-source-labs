# 文字列をスネークケースに変換する関数

文字列をスネークケースに変換するには、次の関数を使用します。

```js
const toSnakeCase = (str) => {
  if (!str) return "";
  const regex =
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
  return str
    .match(regex)
    .map((x) => x.toLowerCase())
    .join("_");
};
```

この関数は、適切な正規表現を使用して `String.prototype.match()` を使って文字列を単語に分解します。そして、単語を結合して `_` を区切り文字として追加するために、`Array.prototype.map()`、`Array.prototype.slice()`、`Array.prototype.join()`、および `String.prototype.toLowerCase()` を使用します。

使用例:

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); // 'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
