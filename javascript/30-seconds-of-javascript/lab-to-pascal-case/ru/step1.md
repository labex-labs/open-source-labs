# Функция для преобразования строки в Pascal case

Для преобразования строки в Pascal case вы можете использовать функцию `toPascalCase()`. Вот как это сделать:

- Сначала откройте Терминал/SSH и введите `node`, чтобы начать практиковать программирование.
- Затем используйте метод `String.prototype.match()` с соответствующим регулярным выражением, чтобы разбить строку на слова.
- Далее используйте методы `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toUpperCase()` и `String.prototype.toLowerCase()`, чтобы объединить слова, сделав первую букву каждого слова заглавной, а остальные - строчными.
- Наконец, вызовите функцию `toPascalCase()` с нужной вам строкой в качестве аргумента, чтобы преобразовать ее в Pascal case.

Вот код функции `toPascalCase()`:

```js
const toPascalCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.charAt(0).toUpperCase() + x.slice(1).toLowerCase())
    .join("");
```

Вы можете использовать эту функцию для преобразования любой строки в Pascal case. Вот несколько примеров:

```js
toPascalCase("some_database_field_name"); // 'SomeDatabaseFieldName'
toPascalCase("Some label that needs to be pascalized"); // 'SomeLabelThatNeedsToBePascalized'
toPascalCase("some-javascript-property"); // 'SomeJavascriptProperty'
toPascalCase("some-mixed_string with spaces_underscores-and-hyphens"); // 'SomeMixedStringWithSpacesUnderscoresAndHyphens'
```
