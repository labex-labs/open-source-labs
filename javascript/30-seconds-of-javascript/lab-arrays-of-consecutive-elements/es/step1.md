# Encontrando arrays de elementos consecutivos

Para encontrar arrays de elementos consecutivos, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.slice()` para crear un array con `n - 1` elementos eliminados desde el principio.
3. Utiliza `Array.prototype.map()` y `Array.prototype.slice()` para mapear cada elemento a un array de `n` elementos consecutivos.

Aquí hay una función de ejemplo que implementa estos pasos:

```js
const findConsecutive = (arr, n) =>
  arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

Puedes llamar a esta función con un array y un número `n` para encontrar todos los arrays de `n` elementos consecutivos en el array. Por ejemplo:

```js
findConsecutive([1, 2, 3, 4, 5], 2);
// [[1, 2], [2, 3], [3, 4], [4, 5]]
```
