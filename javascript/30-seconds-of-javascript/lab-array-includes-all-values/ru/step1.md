# Функция для проверки, содержит ли массив все значения

Если вы хотите проверить, все ли элементы массива `values` содержатся в другом массиве `arr`, вы можете использовать функцию `includesAll` на JavaScript.

Для начала использовать функцию, откройте Терминал/SSH и введите `node`.

Вот, как работает функция `includesAll`:

- Она использует методы `Array.prototype.every()` и `Array.prototype.includes()` для проверки, все ли элементы в `values` содержатся в `arr`.
- Если все элементы в `values` содержатся в `arr`, функция вернет `true`. В противном случае она вернет `false`.

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

Вот пример использования функции `includesAll`:

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
