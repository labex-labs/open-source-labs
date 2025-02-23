# Eliminación de elementos de un array desde la derecha basado en una función

Para eliminar elementos del final de un array hasta que se cumpla una cierta condición, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Recorra el array utilizando `Array.prototype.slice()` para eliminar el último elemento del array hasta que la `func` pasada devuelva `true`.
3. Devuelva los elementos restantes del array.

A continuación, se muestra una implementación de ejemplo:

```js
const dropRightWhile = (arr, func) => {
  let rightIndex = arr.length;
  while (rightIndex-- && !func(arr[rightIndex]));
  return arr.slice(0, rightIndex + 1);
};
```

Puede utilizar esta función de la siguiente manera:

```js
dropRightWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
