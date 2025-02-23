# Проверить, является ли значение асинхронной функцией в JavaScript

Для проверки того, является ли значение асинхронной функцией в JavaScript, вы можете использовать следующий код:

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

эта функция использует `Object.prototype.toString()` и `Function.prototype.call()` для проверки того, является ли заданный аргумент асинхронной функцией.

Вы можете протестировать функцию, передав в качестве аргументов обычную функцию и асинхронную функцию:

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

Для начала практики программирования на JavaScript откройте Терминал/SSH и введите `node`.
