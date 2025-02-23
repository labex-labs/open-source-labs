# Comprobar si una matriz incluye algún valor

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Para comprobar si una matriz incluye al menos un elemento de otra matriz, utiliza `Array.prototype.some()` y `Array.prototype.includes()`. Aquí hay una función de ejemplo:

```js
const includesAny = (arr, values) => values.some((v) => arr.includes(v));
```

Puedes llamar a esta función y pasarle como argumentos las dos matrices que quieres comparar. La función devolverá un valor booleano que indica si al menos un elemento de `values` está incluido en `arr`. Aquí hay algunos ejemplos:

```js
includesAny([1, 2, 3, 4], [2, 9]); // true
includesAny([1, 2, 3, 4], [8, 9]); // false
```
