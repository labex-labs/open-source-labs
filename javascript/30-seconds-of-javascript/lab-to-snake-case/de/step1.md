# Funktion zum Konvertieren eines Strings in snake case

Um einen String in snake case umzuwandeln, verwenden Sie die folgende Funktion:

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

Diese Funktion verwendet `String.prototype.match()`, um den String mit einem geeigneten regulären Ausdruck in Wörter aufzuteilen. Anschließend verwendet sie `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` und `String.prototype.toLowerCase()`, um die Wörter zu kombinieren und `_` als Trennzeichen hinzuzufügen.

Beispielverwendung:

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); //'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
//'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
