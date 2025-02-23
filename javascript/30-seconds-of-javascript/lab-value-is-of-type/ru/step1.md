# Функция для проверки типа значения

Для проверки того, является ли предоставленное значение определенного типа, следуйте следующим шагам:

- Убедитесь, что значение не является `undefined` или `null`, используя `Array.prototype.includes()`.
- Используйте `Object.prototype.constructor` для сравнения свойства конструктора на значении с указанным `type`.
- Функция `is()` ниже выполняет эти проверки и возвращает `true`, если значение является указанного типа, и `false` в противном случае.

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

Вы можете использовать `is()` для проверки, является ли значение различными типами, такими как `Array`, `ArrayBuffer`, `Map`, `RegExp`, `Set`, `WeakMap`, `WeakSet`, `String`, `Number` и `Boolean`. Например:

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
