# Invocar Funciones con Argumentos

Para ejecutar código usando Node.js, abre la Terminal/SSH y escribe `node`.

Para crear una función que invoque cada función proporcionada con los argumentos que recibe y devuelva los resultados:

- Utiliza `Array.prototype.map()` y `Function.prototype.apply()` para aplicar cada función a los argumentos dados.

```js
const over =
  (...fns) =>
  (...args) =>
    fns.map((fn) => fn.apply(null, args));
```

Ejemplo:

```js
const minMax = over(Math.min, Math.max);
minMax(1, 2, 3, 4, 5); // [1, 5]
```
