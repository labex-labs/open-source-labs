# Algoritmo de Búsqueda Binaria

Para comenzar la práctica de codificación, abre la Terminal/SSH y escribe `node`. El algoritmo de búsqueda binaria se utiliza para encontrar el índice de un elemento dado en una matriz ordenada. Estos son los pasos para implementar el algoritmo de búsqueda binaria:

1. Declara los límites de búsqueda izquierdo y derecho, `l` y `r`, inicializados en `0` y la `longitud` de la matriz respectivamente.
2. Utiliza un bucle `while` para reducir repetidamente la submatriz de búsqueda dividiéndola por la mitad utilizando `Math.floor()`.
3. Si se encuentra el elemento, devuelve su índice. De lo contrario, devuelve `-1`.
4. Tenga en cuenta que este algoritmo no tiene en cuenta los valores duplicados en la matriz.

A continuación, se muestra una implementación de ejemplo del algoritmo de búsqueda binaria en JavaScript:

```js
const binarySearch = (arr, item) => {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    const guess = arr[mid];
    if (guess === item) return mid;
    if (guess > item) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
};
```

Puedes probar la función `binarySearch` con los siguientes ejemplos:

```js
binarySearch([1, 2, 3, 4, 5], 1); // 0
binarySearch([1, 2, 3, 4, 5], 5); // 4
binarySearch([1, 2, 3, 4, 5], 6); // -1
```
