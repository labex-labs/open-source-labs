# Проверка ключей объекта

Для того чтобы убедиться, что все ключи в объекте соответствуют заданным `ключам`, следуйте шагам:

- Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
- Используйте `Object.keys()`, чтобы получить ключи объекта, `obj`.
- Используйте `Array.prototype.every()` и `Array.prototype.includes()`, чтобы проверить, что каждый ключ в объекте содержится в массиве `ключей`.

Вот пример реализации:

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

Вы можете использовать функцию так:

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
