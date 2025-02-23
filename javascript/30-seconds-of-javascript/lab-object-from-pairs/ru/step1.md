# Создание объекта из пар ключ-значение

Для создания объекта из пар ключ-значение используйте функцию `objectFromPairs`.

- Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
- Функция использует `Array.prototype.reduce()`, чтобы создать и объединить пары ключ-значение.
- Для более простой реализации вы также можете использовать [`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries).

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

Пример использования:

```js
objectFromPairs([
  ["a", 1],
  ["b", 2]
]); // {a: 1, b: 2}
```
