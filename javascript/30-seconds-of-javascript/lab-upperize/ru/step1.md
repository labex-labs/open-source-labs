# Как преобразовать ключи объекта в верхний регистр на JavaScript

Для преобразования всех ключей объекта в верхний регистр на JavaScript следуйте этим шагам:

1. Используйте метод `Object.keys()`, чтобы получить массив ключей объекта.
2. Используйте метод `Array.prototype.reduce()`, чтобы преобразовать массив в объект.
3. Используйте метод `String.prototype.toUpperCase()`, чтобы преобразовать ключи в верхний регистр.

Вот код:

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

Для тестирования функции вы можете вызвать ее следующим образом:

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
