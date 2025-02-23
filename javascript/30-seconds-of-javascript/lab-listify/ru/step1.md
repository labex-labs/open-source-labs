# Как преобразовать объект в массив в JavaScript

Чтобы преобразовать объект в массив в JavaScript, можно использовать функцию `listify()`. Вот, как это можно сделать:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.

2. Используйте `Object.entries()`, чтобы получить массив пар ключ-значение объекта.

3. Используйте `Array.prototype.reduce()`, чтобы преобразовать массив в объект.

4. Используйте `mapFn`, чтобы преобразовать ключи и значения объекта, а `Array.prototype.push()`, чтобы добавить преобразованные значения в массив.

Вот код для функции `listify()`:

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

Вот пример, как использовать ее с объектом под названием `people`:

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

С помощью этой функции можно легко преобразовать объект в массив в JavaScript.
