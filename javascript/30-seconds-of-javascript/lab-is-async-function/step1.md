# Value Is Async Function

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if the given argument is an `async` function.

- Use `Object.prototype.toString()` and `Function.prototype.call()` and check if the result is `'[object AsyncFunction]'`.

```js
const isAsyncFunction = val =>
  Object.prototype.toString.call(val) === '[object AsyncFunction]';
```

```js
isAsyncFunction(function() {}); // false
isAsyncFunction(async function() {}); // true
```
