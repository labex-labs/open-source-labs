# Как проверить, наступил ли один день раньше другого в JavaScript

Чтобы проверить, наступил ли один день раньше другого в JavaScript, можно использовать оператор меньше (`<`). Вот пример функции, которая принимает два даты и возвращает логическое значение, указывающее, наступил ли первый день раньше второго:

```js
const isBeforeDate = (dateA, dateB) => dateA < dateB;
```

Можно использовать эту функцию, чтобы проверить, наступил ли определенный день раньше другого дня, передав в качестве аргументов два объекта `Date`. Например:

```js
isBeforeDate(new Date(2010, 10, 20), new Date(2010, 10, 21)); // true
```
