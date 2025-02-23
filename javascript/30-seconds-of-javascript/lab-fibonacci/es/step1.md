# Secuencia de Fibonacci

Para generar la secuencia de Fibonacci en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node`.
2. Utilice `Array.from()` para crear una matriz vacía de la longitud específica, inicializando los primeros dos valores (`0` y `1`).
3. Utilice `Array.prototype.reduce()` y `Array.prototype.concat()` para agregar valores a la matriz, utilizando la suma de los últimos dos valores, excepto los primeros dos.
4. Llame a la función `fibonacci()` y pase la longitud deseada de la secuencia como argumento.

Aquí está el código:

```js
const fibonacci = (n) =>
  Array.from({ length: n }).reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  );

fibonacci(6); // [0, 1, 1, 2, 3, 5]
```

Esto generará una matriz que contiene la secuencia de Fibonacci hasta el término n.
