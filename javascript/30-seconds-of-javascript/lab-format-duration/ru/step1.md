# Форматирование длительности

Для получения человекочитаемого формата заданного количества миллисекунд следуйте шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Разделите `ms` на соответствующие значения, чтобы получить соответствующие значения для `day`, `hour`, `minute`, `second` и `millisecond`.
3. Используйте `Object.entries()` с `Array.prototype.filter()`, чтобы оставить только ненулевые значения.
4. Создайте строку для каждого значения, правильно формируя множественное число, используя `Array.prototype.map()`.
5. Объедините значения в строку, используя `Array.prototype.join()`.

Вот код:

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

Вот несколько примеров:

```js
formatDuration(1001); // '1 second, 1 millisecond'
formatDuration(34325055574);
// '397 days, 6 hours, 44 minutes, 15 seconds, 574 milliseconds'
```
