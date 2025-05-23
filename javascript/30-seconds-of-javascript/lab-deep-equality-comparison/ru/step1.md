# Как проверить равенство объектов в JavaScript

Чтобы проверить, равны ли два значения, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Проведите глубокое сравнение между двумя значениями с использованием функции `equals()`.
3. Проверьте, идентичны ли два значения. Если да, верните `true`.
4. Проверьте, являются ли оба значения объектами `Date` с одинаковым временем, используя `Date.prototype.getTime()`. Если да, верните `true`.
5. Проверьте, являются ли оба значения не-объектными значениями с равными значениями (строгая сравнение). Если да, верните `true`.
6. Проверьте, является ли только одно значение `null` или `undefined`, или отличаются ли их прототипы. Если да, верните `false`.
7. Если ни одно из вышеперечисленных условий не выполняется, используйте `Object.keys()`, чтобы проверить, имеют ли оба значения одинаковое количество ключей.
8. Используйте `Array.prototype.every()`, чтобы проверить, существует ли каждый ключ в `a` в `b` и являются ли они равными при рекурсивном вызове `equals()`.

Используйте следующий код для реализации функции `equals()`:

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

Используйте следующие примеры кода, чтобы протестировать функцию `equals()`:

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
