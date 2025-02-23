# Función para Devolver el Valor Mínimo de una Matriz

Para comenzar a practicar la codificación, abra la Terminal/SSH y escriba `node`.

Esta función devuelve el valor mínimo de una matriz, basado en la función proporcionada.

Para hacer esto, utiliza `Array.prototype.map()` para asignar a cada elemento el valor devuelto por la función. Luego utiliza `Math.min()` para obtener el valor mínimo.

```js
const minBy = (arr, fn) =>
  Math.min(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

Puede usar esta función pasando una matriz y una función. Por ejemplo:

```js
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 2
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 2
```
