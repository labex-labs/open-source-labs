# Descripción del último índice de inserción en una matriz ordenada

Para encontrar el índice más alto donde un valor debe insertarse en una matriz para mantener su orden de clasificación, siga estos pasos:

- Primero, verifique de manera aproximada si la matriz está ordenada en orden descendente.
- Luego, use `Array.prototype.reverse()` y `Array.prototype.findIndex()` para encontrar el último índice adecuado donde se debe insertar el elemento.

A continuación, se muestra el código de la función:

```js
const sortedLastIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr
    .reverse()
    .findIndex((el) => (isDescending ? n <= el : n >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

Y aquí hay un ejemplo de cómo usar la función:

```js
sortedLastIndex([10, 20, 30, 30, 40], 30); // 4
```

Para comenzar a practicar la codificación, abra la Terminal/SSH y escriba `node`.
