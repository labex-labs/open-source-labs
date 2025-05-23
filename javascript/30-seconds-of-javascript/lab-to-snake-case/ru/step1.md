# Функция для преобразования строки в snake case

Для преобразования строки в snake case используйте следующую функцию:

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

Эта функция использует `String.prototype.match()`, чтобы разбить строку на слова с использованием соответствующего регулярного выражения. Затем она использует `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` и `String.prototype.toLowerCase()`, чтобы объединить слова, добавляя `_` в качестве разделителя.

Пример использования:

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); //'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
//'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
