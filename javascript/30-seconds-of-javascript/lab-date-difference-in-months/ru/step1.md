# Функция для вычисления разницы между датами в месяцах

Для вычисления разницы между двумя датами в месяцах используйте следующую функцию:

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0
  );
```

Для использования этой функции передайте два объекта `Date` в качестве аргументов. Например:

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

Эта функция использует методы `Date.prototype.getFullYear()` и `Date.prototype.getMonth()` для вычисления разницы между двумя датами в месяцах.
