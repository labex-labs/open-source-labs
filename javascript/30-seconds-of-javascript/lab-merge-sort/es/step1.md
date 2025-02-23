# Algoritmo de clasificación Merge

Para practicar la codificación utilizando el algoritmo de clasificación Merge, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node`.
2. Utiliza la recursividad para ordenar una matriz de números.
3. Si la `longitud` de la matriz es menor que `2`, devuelve la matriz.
4. Utiliza `Math.floor()` para calcular el punto medio de la matriz.
5. Utiliza `Array.prototype.slice()` para dividir la matriz en dos y llama recursivamente a `mergeSort()` en las submatrices creadas.
6. Finalmente, utiliza `Array.from()` y `Array.prototype.shift()` para combinar las dos submatrices ordenadas en una.

Aquí está el código:

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

Prueba con este ejemplo:

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
