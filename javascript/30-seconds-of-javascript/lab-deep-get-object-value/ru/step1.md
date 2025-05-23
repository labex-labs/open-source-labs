# Как получить вложенное значение в объекте с использованием массива ключей

Для получения конкретного значения из вложенного JSON-объекта можно использовать функцию `deepGet`. Эта функция принимает объект и массив ключей и возвращает целевой элемент, если он существует в объекте.

Для использования функции `deepGet`:

- Создайте массив ключей, которые вы хотите получить из вложенного JSON-объекта.
- Вызовите функцию `deepGet` с объектом и массивом ключей.
- Функция вернет целевой элемент, если он существует, или `null`, если не существует.

Вот код для функции `deepGet`:

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

Вот пример использования функции `deepGet`:

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // возвращает 3
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // возвращает null
```

Для начала практики программирования откройте Терминал/SSH и введите `node`.
