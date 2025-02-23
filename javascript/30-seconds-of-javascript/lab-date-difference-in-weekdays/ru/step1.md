# Подсчет рабочих дней между двумя датами

Для подсчета рабочих дней между двумя датами следуйте шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте `Array.from()`, чтобы создать массив с длиной, равной количеству дней между `startDate` и `endDate`.
3. Используйте `Array.prototype.reduce()`, чтобы перебрать массив, проверяя, является ли каждая дата рабочим днем, и увеличивать `count`.
4. Обновите `startDate` следующим днем на каждой итерации с использованием `Date.prototype.getDate()` и `Date.prototype.setDate()`, чтобы продвинуть ее на один день.
5. Обратите внимание, что эта функция не учитывает официальные праздники.

Вот код для реализации этого:

```js
const countWeekDaysBetween = (startDate, endDate) =>
  Array.from({ length: (endDate - startDate) / (1000 * 3600 * 24) }).reduce(
    (count) => {
      if (startDate.getDay() % 6 !== 0) count++;
      startDate = new Date(startDate.setDate(startDate.getDate() + 1));
      return count;
    },
    0
  );
```

Вы можете использовать следующий код для тестирования функции:

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
