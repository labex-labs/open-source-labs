# Найти соответствующие ключи

Для поиска всех ключей в объекте, которые соответствуют заданному значению, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковать программирование.
2. Используйте `Object.keys()`, чтобы получить все свойства объекта.
3. Используйте `Array.prototype.filter()`, чтобы проверить каждую пару ключ-значение и вернуть все ключи, которые равны заданному значению.

Вот пример функции, которая реализует эту логику:

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

Вы можете использовать эту функцию так:

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
