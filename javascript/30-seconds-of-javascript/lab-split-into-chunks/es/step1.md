# Cómo dividir una matriz en trozos de un tamaño específico

Para practicar la codificación, abre la Terminal/SSH y escribe `node`.

Para dividir una matriz en matrices más pequeñas de un tamaño especificado, sigue estos pasos:

1. Utiliza `Array.from()` para crear una nueva matriz que ajuste al número de trozos que se producirán.
2. Utiliza `Array.prototype.slice()` para mapear cada elemento de la nueva matriz a un trozo de longitud `size`.
3. Si la matriz original no se puede dividir uniformemente, el último trozo contendrá los elementos restantes.

Aquí hay un fragmento de código de ejemplo:

```js
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
```

Puedes utilizar esta función pasando la matriz que quieres dividir y el tamaño deseado de los trozos. Por ejemplo:

```js
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```
