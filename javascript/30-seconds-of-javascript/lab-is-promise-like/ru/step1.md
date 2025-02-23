# JavaScript Promises

Для проверки того, является ли объект похож на Promise, используйте функцию `isPromiseLike`. Эта функция проверяет, не является ли объект null, имеет ли тип object или function и имеет ли свойство `.then`, которое также является функцией.

Вот код для `isPromiseLike`:

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

Вот несколько примеров использования `isPromiseLike`:

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

Для начала практики программирования на JavaScript откройте Терминал/SSH и введите `node`.
