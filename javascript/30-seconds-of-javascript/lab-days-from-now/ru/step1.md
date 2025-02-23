# Функция для вычисления даты, которая наступит через 'n' дней от текущей

Для вычисления даты, которая наступит через 'n' дней от текущей, следуйте шагам:

- Откройте Терминал/SSH и введите 'node', чтобы начать практиковаться в написании кода.
- Используйте конструктор `Date`, чтобы получить текущую дату.
- Используйте `Math.abs()` и `Date.prototype.getDate()`, чтобы соответствующим образом обновить дату.
- Установите результат с использованием `Date.prototype.setDate()`.
- Используйте `Date.prototype.toISOString()`, чтобы вернуть строку в формате `yyyy-mm-dd`.

Вот код:

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

Пример использования:

```js
daysFromNow(5); // Output: 2020-10-13 (если текущая дата 2020-10-08)
```
