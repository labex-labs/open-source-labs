# Функция для определения размера массива, объекта или строки

Для использования этой функции откройте Терминал/SSH и введите `node`. Эта функция определяет размер массива, объекта или строки.

Для ее использования:

- Определите тип `val` (`массив`, `объект` или `строка`).
- Используйте свойство `Array.prototype.length` для массивов.
- Используйте значение `length` или `size`, если оно доступно, или количество ключей для объектов.
- Для строк используйте `размер` объекта [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob), созданного из `val`.

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
      ? val.size || val.length || Object.keys(val).length
      : typeof val === "string"
        ? new Blob([val]).size
        : 0;
```

Примеры:

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
