# Cómo llamar a funciones con contexto en JavaScript

Para ejecutar código en Node.js, abre la Terminal/SSH y escribe `node`. Si quieres llamar a una función con un contexto específico y un conjunto de argumentos en JavaScript, puedes utilizar una clausura. Aquí te muestro cómo hacerlo:

1. Define una función llamada `call` que tome una `clave` y un conjunto de `argumentos` como parámetros y devuelva una nueva función que tome un parámetro `contexto`.

```js
const call =
  (key, ...args) =>
  (context) =>
    context[key](...args);
```

2. Utiliza la función `call` para llamar a la función `map` en una matriz de números. En este ejemplo, la función `map` duplica cada número de la matriz.

```js
Promise.resolve([1, 2, 3])
  .then(call("map", (x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

3. También puedes enlazar la función `call` a una clave específica, como `map`, y utilizarla para llamar a la función `map` en una matriz de números.

```js
const map = call.bind(null, "map");
Promise.resolve([1, 2, 3])
  .then(map((x) => 2 * x))
  .then(console.log); // [ 2, 4, 6 ]
```

Al utilizar la función `call`, puedes llamar fácilmente a cualquier función con un contexto específico y un conjunto de argumentos.
