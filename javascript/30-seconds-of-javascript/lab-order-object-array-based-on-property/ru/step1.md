# Как упорядочить массив объектов в соответствии с порядком свойств

Для упорядочивания массива объектов в соответствии с порядком свойств следуйте следующим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте `Array.prototype.reduce()`, чтобы создать объект из массива `order`, где значения будут ключами, а их исходный индекс - значением.
3. Используйте `Array.prototype.sort()`, чтобы отсортировать заданный массив, пропуская элементы, для которых `prop` пуст или не находится в массиве `order`.

Вот примерный код для упорядочивания массива объектов в соответствии с порядком свойств:

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

Вы можете использовать функцию `orderWith`, чтобы упорядочить массив объектов в соответствии с порядком свойств. Например:

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" }
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
