# JavaScript-функция для проверки, является ли строка анаграммой

Для проверки, является ли строка анаграммой другой строки, используйте следующую JavaScript-функцию. Она нечувствительна к регистру и игнорирует пробелы, знаки препинания и специальные символы.

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

Для использования функции откройте Терминал/SSH и введите `node`. Затем вызовите функцию с двумя строками в качестве аргументов:

```js
isAnagram("iceman", "cinema"); // true
```

Функция использует `String.prototype.toLowerCase()` и `String.prototype.replace()` с соответствующим регулярным выражением для удаления ненужных символов. Она также использует `String.prototype.split()`, `Array.prototype.sort()` и `Array.prototype.join()` для обеих строк, чтобы нормализовать их и проверить, равны ли их нормализованные формы.
