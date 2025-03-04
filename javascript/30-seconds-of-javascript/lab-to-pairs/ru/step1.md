# Преобразование объекта в пары

Для преобразования объекта в массив пар ключ-значение используйте функцию `toPairs`. Чтобы приступить к программированию, откройте Терминал/SSH и введите `node`.

Функция `toPairs` работает следующим образом:

- Во - первых, она проверяет, определена ли `Symbol.iterator` для заданного итерируемого объекта.
- Если `Symbol.iterator` определена, она использует `Array.prototype.entries()`, чтобы получить итератор для объекта, а затем преобразует результат в массив массивов пар ключ-значение с использованием `Array.from()`.
- Если для объекта не определена `Symbol.iterator`, она использует `Object.entries()` вместо этого.

Вот код для функции `toPairs`:

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

Вы можете использовать функцию `toPairs` с различными типами объектов, такими как:

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0','s'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
