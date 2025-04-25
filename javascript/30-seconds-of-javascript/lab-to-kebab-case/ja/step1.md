# 文字列をケバブケースに変換する

文字列をケバブケースに変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `String.prototype.match()` を使用して、適切な正規表現を使って文字列を単語に分割します。
3. `Array.prototype.map()`、`Array.prototype.join()`、および `String.prototype.toLowerCase()` を使用して、単語を結合し、区切り文字として `-` を追加します。

以下は、変換を行う例の関数です。

```js
const toKebabCase = (str) =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.toLowerCase())
    .join("-");
```

次のように、この関数を使用して文字列をケバブケースに変換できます。

```js
toKebabCase("camelCase"); // 'camel-case'
toKebabCase("some text"); // 'some-text'
toKebabCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some-mixed-string-with-spaces-underscores-and-hyphens'
toKebabCase("AllThe-small Things"); // 'all-the-small-things'
toKebabCase("IAmEditingSomeXMLAndHTML");
// 'i-am-editing-some-xml-and-html'
```
