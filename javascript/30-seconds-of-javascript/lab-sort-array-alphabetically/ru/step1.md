# Как сортировать массив по алфавиту на основе заданного свойства в JavaScript

Чтобы сортировать массив объектов по алфавиту на основе заданного свойства в JavaScript, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковать программирование.
2. Используйте `Array.prototype.sort()`, чтобы отсортировать массив на основе заданного свойства.
3. Используйте `String.prototype.localeCompare()`, чтобы сравнить значения заданного свойства.

Вот пример кода, который вы можете использовать:

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

Вы можете вызвать функцию `alphabetical` с массивом объектов и функцией-генератором, которая возвращает свойство для сортировки. Вот пример использования:

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
