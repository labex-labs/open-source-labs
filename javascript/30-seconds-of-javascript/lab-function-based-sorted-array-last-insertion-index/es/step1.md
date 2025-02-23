# Cómo encontrar el último índice de inserción en una matriz ordenada en función de una función

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

A continuación, se muestra cómo encontrar el índice más alto en el que se debe insertar un valor en una matriz para mantener su orden de clasificación, en función de una función iteradora proporcionada:

1. Comprueba si la matriz está ordenada en orden descendente.
2. Utiliza `Array.prototype.map()` para aplicar la función iteradora a todos los elementos de la matriz.
3. Utiliza `Array.prototype.reverse()` y `Array.prototype.findIndex()` para encontrar el último índice adecuado donde se debe insertar el elemento, en función de la función iteradora proporcionada.

Ve el código siguiente:

```js
const sortedLastIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr
    .map(fn)
    .reverse()
    .findIndex((el) => (isDescending ? val <= el : val >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

Aquí hay un ejemplo:

```js
sortedLastIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, (o) => o.x); // 1
```
