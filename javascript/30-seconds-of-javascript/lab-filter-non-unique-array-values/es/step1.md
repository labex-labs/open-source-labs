# Cómo filtrar valores no únicos en una matriz en JavaScript

Para filtrar valores no únicos en una matriz en JavaScript, puedes crear una nueva matriz con solo los valores únicos. Aquí está cómo:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el constructor `Set` y el operador de propagación (`...`) para crear una matriz con los valores únicos de la matriz original.
3. Utiliza `Array.prototype.filter()` para crear una matriz que contenga solo los valores únicos.

Aquí hay una función de ejemplo que hace esto:

```js
const filterNonUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) === arr.lastIndexOf(i));
```

Puedes utilizar esta función con cualquier matriz para filtrar los valores no únicos. Por ejemplo:

```js
filterNonUnique([1, 2, 2, 3, 4, 4, 5]); // [1, 3, 5]
```
