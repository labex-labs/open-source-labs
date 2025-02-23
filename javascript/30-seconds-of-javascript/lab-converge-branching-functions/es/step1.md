# Funciones convergentes

Para practicar la codificación, abre la Terminal/SSH y escribe `node`.

Esta función `converge` toma una función convergente y una lista de funciones de bifurcación como entrada. Devuelve una nueva función que aplica cada función de bifurcación a los argumentos de entrada. Los resultados de las funciones de bifurcación se pasan luego como argumentos a la función convergente.

Los métodos `Array.prototype.map()` y `Function.prototype.apply()` se utilizan para aplicar cada función a los argumentos de entrada. El operador de propagación (`...`) se utiliza luego para llamar a `converger` con los resultados de todas las demás funciones.

Aquí está el código para la función `converge`:

```js
const converge =
  (converger, fns) =>
  (...args) =>
    converger(...fns.map((fn) => fn.apply(null, args)));
```

Un ejemplo de cómo utilizar esta función se muestra a continuación. La función `average` se crea llamando a `converge` con una función anónima que calcula el promedio de una matriz. Las funciones de bifurcación son dos funciones anónimas que calculan la suma de una matriz y su longitud, respectivamente.

```js
const average = converge(
  (a, b) => a / b,
  [(arr) => arr.reduce((a, v) => a + v, 0), (arr) => arr.length]
);
average([1, 2, 3, 4, 5, 6, 7]); // 4
```

Este código calcula el promedio de la matriz `[1, 2, 3, 4, 5, 6, 7]` y devuelve `4`.
