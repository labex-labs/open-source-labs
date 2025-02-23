# Генератор диапазона дат

Для генерации всех дат в заданном диапазоне с заданным шагом используйте следующий код в Терминале/SSH и введите `node`:

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

Это создает генератор, который использует цикл `while` для итерации от `start` до `end`, используя конструктор `Date` для возврата каждой даты в диапазоне и увеличивая на `step` дней с использованием `Date.prototype.getDate()` и `Date.prototype.setDate()`.

Чтобы использовать значение по умолчанию `1` для `step`, опустите третий аргумент.

Вот пример использования `dateRangeGenerator`:

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
