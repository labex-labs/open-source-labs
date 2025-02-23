# Clasificación de Arrays

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Esta función calcula la clasificación de un array basado en una función comparadora.

Para utilizar esta función, puedes:

- Utilizar `Array.prototype.map()` y `Array.prototype.filter()` para asignar a cada elemento una clasificación utilizando la función comparadora proporcionada.

Aquí hay un ejemplo de uso:

```js
const ranking = (arr, compFn) =>
  arr.map((a) => arr.filter((b) => compFn(a, b)).length + 1);
```

Ejemplo:

```js
ranking([8, 6, 9, 5], (a, b) => a < b);
// [2, 3, 1, 4]
ranking(["c", "a", "b", "d"], (a, b) => a.localeCompare(b) > 0);
// [3, 1, 2, 4]
```
