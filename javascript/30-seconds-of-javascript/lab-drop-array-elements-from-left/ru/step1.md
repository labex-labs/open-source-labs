# Удаление элементов массива слева

Для начала практики программирования откройте Терминал/SSH и введите `node`.

Вот функция, которая создает новый массив с удалением заданного количества элементов слева:

```js
const drop = (arr, n = 1) => arr.slice(n);
```

Функция использует `Array.prototype.slice()` для удаления заданного количества элементов слева. Если вы опустите последний аргумент `n`, функция будет использовать значение по умолчанию `1`.

Вот несколько примеров использования функции `drop`:

```js
drop([1, 2, 3]); // [2, 3]
drop([1, 2, 3], 2); // [3]
drop([1, 2, 3], 42); // []
```
