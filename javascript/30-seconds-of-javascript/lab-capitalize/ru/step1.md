# JavaScript-функция для перевода первой буквы строки в верхний регистр

Для перевода первой буквы строки в верхний регистр в JavaScript используйте следующую функцию:

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

Эта функция использует деструктуризацию массива и `String.prototype.toUpperCase()`, чтобы перевести первую букву строки в верхний регистр. Аргумент `lowerRest` является необязательным и может быть установлен в `true`, чтобы перевести остальную часть строки в нижний регистр.

Вот пример использования этой функции:

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
