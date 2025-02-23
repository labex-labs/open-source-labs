# Как упорядочить массив объектов в JavaScript

Для упорядочивания массива объектов в JavaScript можно использовать метод `Array.prototype.sort()` и метод `Array.prototype.reduce()` на массиве `props` со значением по умолчанию `0`.

Вот пример функции `orderBy`, которая сортирует массив объектов в соответствии с указанными свойствами и порядками:

```js
const orderBy = (arr, props, orders = ["asc"]) =>
  [...arr].sort((a, b) =>
    props.reduce((acc, prop, i) => {
      if (acc === 0) {
        const [p1, p2] =
          orders[i] === "desc" ? [b[prop], a[prop]] : [a[prop], b[prop]];
        acc = p1 > p2 ? 1 : p1 < p2 ? -1 : 0;
      }
      return acc;
    }, 0)
  );
```

Для использования этой функции передайте массив объектов, массив свойств для сортировки и необязательный массив порядков. Если массив `orders` не передан, функция по умолчанию будет сортировать по `'asc'`.

Вот несколько примеров использования функции `orderBy`:

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// сортировать по имени по возрастанию и по возрасту по убыванию
orderBy(users, ["name", "age"], ["asc", "desc"]);
// Вывод: [{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// сортировать по имени по возрастанию и по возрасту по возрастанию (стандартный порядок)
orderBy(users, ["name", "age"]);
// Вывод: [{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
