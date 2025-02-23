# Índice de todas las coincidencias

Para encontrar todos los índices de `val` en una matriz, utiliza `Array.prototype.reduce()` para recorrer los elementos y almacenar los índices de los elementos que coinciden. Si `val` nunca aparece, se devuelve una matriz vacía.

```js
const indexOfAll = (arr, val) =>
  arr.reduce((acc, el, i) => (el === val ? [...acc, i] : acc), []);
```

Uso de ejemplo:

```js
indexOfAll([1, 2, 3, 1, 2, 3], 1); // [0, 3]
indexOfAll([1, 2, 3], 4); // []
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Este es un índice de todas las coincidencias.
