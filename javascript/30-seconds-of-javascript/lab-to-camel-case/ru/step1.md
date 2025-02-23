# Преобразование строки в camelCase

Чтобы преобразовать строку в camelCase, следуйте следующим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте `String.prototype.match()` с соответствующим регулярным выражением, чтобы разбить строку на слова.
3. Используйте `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toLowerCase()` и `String.prototype.toUpperCase()`, чтобы объединить слова и сделать заглавной первую букву каждого из них.
4. Используйте функцию `toCamelCase`, показанную ниже, для выполнения преобразования:

```js
const toCamelCase = (str) => {
  const words =
    str &&
    str.match(
      /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
    );
  const capitalizedWords =
    words &&
    words.map(
      (word) => word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase()
    );
  const camelCaseString = capitalizedWords && capitalizedWords.join("");
  return (
    camelCaseString &&
    camelCaseString.slice(0, 1).toLowerCase() + camelCaseString.slice(1)
  );
};
```

Ниже приведены некоторые примеры использования функции `toCamelCase`:

```js
toCamelCase("some_database_field_name"); // 'someDatabaseFieldName'
toCamelCase("Some label that needs to be camelized");
// 'someLabelThatNeedsToBeCamelized'
toCamelCase("some-javascript-property"); // 'someJavascriptProperty'
toCamelCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'someMixedStringWithSpacesUnderscoresAndHyphens'
```
