# Поиск максимальной даты

Для поиска максимального значения даты из заданного массива дат следуйте этим шагам:

1. Откройте Терминал или SSH.
2. Введите `node`, чтобы начать практиковаться в написании кода.
3. Используйте расширение ES6 с `Math.max()` для поиска максимального значения даты.
4. Преобразуйте максимальное значение даты в объект `Date` с использованием конструктора `Date`.

Вот пример кода:

```js
const maxDate = (...dates) => new Date(Math.max(...dates));

const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];

maxDate(...dates); // Возвращает "2018-03-11T22:00:00.000Z"
```

Следуя этим шагам и используя предоставленный код, вы можете легко найти максимальное значение даты из заданного массива дат.
