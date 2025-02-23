# Función para Aplicar una Función a Elementos Consecutivos en un Array

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

Esta función aplica una función dada `fn` a cada bloque de `n` elementos consecutivos en un array. Sigue estos pasos:

- Utiliza `Array.prototype.slice()` para obtener un nuevo array `arr` con los primeros `n` elementos eliminados.
- Utiliza `Array.prototype.map()` y `Array.prototype.slice()` para aplicar `fn` a cada bloque de `n` elementos consecutivos en `arr`.

Aquí está el código:

```js
const mapConsecutive = (arr, n, fn) =>
  arr.slice(n - 1).map((v, i) => fn(arr.slice(i, i + n)));
```

Por ejemplo, puedes utilizar `mapConsecutive()` para aplicar una función a cada bloque de 3 elementos consecutivos en un array de números, uniendo los elementos con guiones:

```js
mapConsecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, (x) => x.join("-"));
// ['1-2-3', '2-3-4', '3-4-5', '4-5-6', '5-6-7', '6-7-8', '7-8-9', '8-9-10'];
```
