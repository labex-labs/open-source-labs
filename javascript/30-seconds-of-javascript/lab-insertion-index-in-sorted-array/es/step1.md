# Cómo encontrar el índice de inserción en un array ordenado

Para encontrar el índice más bajo en el que un valor debe ser insertado en un array ordenado, siga estos pasos:

1. Verifique si el array está ordenado en orden descendente.
2. Utilice el método `Array.prototype.findIndex()` para encontrar el índice adecuado donde el elemento debe ser insertado.

Aquí está el código para implementar esto:

```js
const sortedIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr.findIndex((el) => (isDescending ? n >= el : n <= el));
  return index === -1 ? arr.length : index;
};
```

Puede llamar a la función `sortedIndex` pasando el array ordenado y el valor que desea insertar. Aquí hay algunos ejemplos:

```js
sortedIndex([5, 3, 2, 1], 4); // Salida: 1
sortedIndex([30, 50], 40); // Salida: 1
```

Al utilizar esta función, puede encontrar fácilmente el índice de inserción de un valor en un array ordenado.
