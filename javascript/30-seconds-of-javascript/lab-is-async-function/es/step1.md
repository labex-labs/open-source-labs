# Comprobar si un valor es una función asíncrona en JavaScript

Para comprobar si un valor es una función `async` en JavaScript, puedes utilizar el siguiente código:

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

Esta función utiliza `Object.prototype.toString()` y `Function.prototype.call()` para comprobar si el argumento dado es una función `async`.

Puedes probar la función pasando una función regular y una función `async` como argumentos:

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

Para comenzar a practicar la programación en JavaScript, abre la Terminal/SSH y escribe `node`.
