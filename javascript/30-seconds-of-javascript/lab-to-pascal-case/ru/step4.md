# Создание полной функции toPascalCase

Теперь, когда мы понимаем все необходимые компоненты, давайте создадим полную функцию `toPascalCase`, которая может обрабатывать любую входную строку.

1. Создадим JavaScript-файл для сохранения нашей функции. Выйдите из сессии Node.js, нажав Ctrl+C дважды или введя `.exit`.

2. В WebIDE создайте новый файл, кликнув "File" > "New File" в верхнем меню.

3. Сохраните файл как `pascalCase.js` в директории `/home/labex/project`.

4. Скопируйте и вставьте следующий код в редактор:

```javascript
/**
 * Converts a string to Pascal case.
 * @param {string} str - The input string to convert.
 * @returns {string} The Pascal cased string.
 */
function toPascalCase(str) {
  // Use regex to match words regardless of delimiter
  const words = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  // If no words are found, return an empty string
  if (!words) {
    return "";
  }

  // Capitalize each word and join them
  return words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// Test cases
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("some_database_field_name")); // "SomeDatabaseFieldName"
console.log(toPascalCase("Some label that needs to be pascalized")); // "SomeLabelThatNeedsToBePascalized"
console.log(toPascalCase("some-javascript-property")); // "SomeJavascriptProperty"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"
```

5. Сохраните файл, нажав Ctrl+S или выбрав "File" > "Save" из меню.

6. Запустите файл с использованием Node.js, открыв терминал и введя:

```bash
node pascalCase.js
```

Вы должны увидеть следующий вывод:

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

Наша функция `toPascalCase` теперь работает правильно. Рассмотрим, как она работает:

1. Мы используем регулярное выражение для нахождения слов во входной строке, независимо от используемых разделителей.
2. Проверяем, были ли найдены какие-либо слова. Если нет, возвращаем пустую строку.
3. Используем метод `map()` для приведения первой буквы каждого слова к верхнему регистру и `join('')` для объединения слов без разделителей.
4. Результатом является строка в формате Pascal case, где каждое слово начинается с заглавной буквы, а остальные буквы - строчные.
