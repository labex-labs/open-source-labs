# Función para calcular la suma de los elementos de un array mapeado

Para calcular la suma de un array al mapear cada elemento a un valor utilizando una función proporcionada, utiliza la función `sumBy`. Esta función utiliza `Array.prototype.map()` para mapear cada elemento al valor devuelto por `fn`. Luego, utiliza `Array.prototype.reduce()` para sumar cada valor a un acumulador, que se inicializa con un valor de `0`.

```js
const sumBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0);
```

Uso de ejemplo:

```js
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // Devuelve 20
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // Devuelve 20
```

Para comenzar a practicar la codificación con esta función, abre la Terminal/SSH y escribe `node`.
