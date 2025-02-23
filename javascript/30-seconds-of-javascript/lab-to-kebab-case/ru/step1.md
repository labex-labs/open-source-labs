# Преобразование строки в «kebab case»

Для преобразования строки в «kebab case» следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте `String.prototype.match()`, чтобы разбить строку на слова с использованием соответствующего регулярного выражения.
3. Используйте `Array.prototype.map()`, `Array.prototype.join()` и `String.prototype.toLowerCase()`, чтобы объединить слова, добавляя `-` в качестве разделителя.

Вот пример функции, которая выполняет преобразование:

```js
const toKebabCase = (str) =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.toLowerCase())
    .join("-");
```

Вы можете использовать эту функцию для преобразования строк в «kebab case», как показано ниже:

```js
toKebabCase("camelCase"); // 'camel-case'
toKebabCase("some text"); //'some-text'
toKebabCase("some-mixed_string With spaces_underscores-and-hyphens");
//'some-mixed-string-with-spaces-underscores-and-hyphens'
toKebabCase("AllThe-small Things"); // 'all-the-small-things'
toKebabCase("IAmEditingSomeXMLAndHTML");
// 'i-am-editing-some-xml-and-html'
```
