# Как заменить или добавить значение в массив

Для замены элемента в массиве или добавления его, если он отсутствует, следуйте шагам:

1. Используйте оператор расширения (`...`), чтобы создать поверхностную копию массива.
2. Используйте `Array.prototype.findIndex()`, чтобы найти индекс первого элемента, который удовлетворяет заданной функции сравнения `compFn`.
3. Если такого элемента не найдено, используйте `Array.prototype.push()`, чтобы добавить новое значение в массив.
4. В противном случае используйте `Array.prototype.splice()`, чтобы заменить значение по найденному индексу новым значением.

Вот пример, как реализовать эту функциональность:

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

Вы можете использовать эту функцию с массивом объектов следующим образом:

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
