# Преобразование дат в формат ISO с учетом часового пояса

Для преобразования даты в расширенный формат ISO (ISO 8601), включая смещение часового пояса, следуйте шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать программирование.
2. Используйте `Date.prototype.getTimezoneOffset()`, чтобы получить смещение часового пояса и перевернуть его. Сохраните его знак в `diff`.
3. Определите вспомогательную функцию `pad()`, которая нормализует любое переданное число до целого с использованием `Math.floor()` и `Math.abs()` и дополняет его до `2` цифр с использованием `String.prototype.padStart()`.
4. Используйте `pad()` и встроенные методы в прототипе `Date`, чтобы построить строку ISO 8601 с смещением часового пояса.

Вот код, который вы можете использовать:

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

Используйте функцию `toISOStringWithTimezone()` с объектом `new Date()` в качестве аргумента, чтобы получить дату в формате ISO с смещением часового пояса. Например:

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
