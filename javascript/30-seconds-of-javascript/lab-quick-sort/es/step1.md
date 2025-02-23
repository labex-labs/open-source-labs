# Algoritmo de Ordenamiento Rápido

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Este algoritmo ordena una matriz de números utilizando el algoritmo de ordenamiento rápido. Estos son los pasos a seguir:

- Utiliza la recursividad.
- Utiliza el operador de propagación (`...`) para clonar la matriz original, `arr`.
- Si la `longitud` de la matriz es menor que `2`, devuelve la matriz clonada.
- Utiliza `Math.floor()` para calcular el índice del elemento pivote.
- Utiliza `Array.prototype.reduce()` y `Array.prototype.push()` para dividir la matriz en dos submatrices. La primera contiene elementos menores o iguales a `pivote`, y la segunda contiene elementos mayores que él. Desestructura el resultado en dos matrices.
- Llama recursivamente a `quickSort()` en las submatrices creadas.

Este es un ejemplo de cómo implementar este algoritmo:

```js
const quickSort = (arr) => {
  const a = [...arr];
  if (a.length < 2) return a;
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = a[pivotIndex];
  const [lo, hi] = a.reduce(
    (acc, val, i) => {
      if (val < pivot || (val === pivot && i != pivotIndex)) {
        acc[0].push(val);
      } else if (val > pivot) {
        acc[1].push(val);
      }
      return acc;
    },
    [[], []]
  );
  return [...quickSort(lo), pivot, ...quickSort(hi)];
};
```

Para probarlo, ejecuta el siguiente comando:

```js
quickSort([1, 6, 1, 5, 3, 2, 1, 4]); // [1, 1, 1, 2, 3, 4, 5, 6]
```
