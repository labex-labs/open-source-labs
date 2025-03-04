# Функция для индексирования массива

Для индексирования массива с использованием функции следуйте шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте `Array.prototype.reduce()`, чтобы создать объект из массива.
3. Примените заданную функцию к каждому значению массива, чтобы получить ключ, и добавьте пару ключ-значение в объект.

Вот пример кода:

```js
const indexBy = (arr, fn) =>
  arr.reduce((obj, v, i) => {
    obj[fn(v, i, arr)] = v;
    return obj;
  }, {});
```

Вы можете использовать эту функцию следующим образом:

```js
indexBy(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  (x) => x.id
);
// { '10': { id: 10, name: 'apple' }, '20': { id: 20, name: 'orange' } }
```

Эта функция создает объект из массива, сопоставляя каждое значение с ключом с использованием заданной функции. Результирующий объект содержит пары ключ-значение, где ключи создаются функцией, а значения — исходные элементы массива.
