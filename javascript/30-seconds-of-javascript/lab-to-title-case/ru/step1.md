# Функция для преобразования строки в заглавный регистр

Для преобразования заданной строки в заглавный регистр используйте следующую функцию. Она использует `String.prototype.match()`, чтобы разбить строку на слова с использованием соответствующего регулярного выражения. Затем она объединяет их с использованием `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` и `String.prototype.toUpperCase()`. Это делает заглавной первую букву каждого слова и добавляет пробел между ними.

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

Вот несколько примеров использования этой функции:

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
