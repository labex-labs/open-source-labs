# Cómo eliminar elementos de un array desde el final en JavaScript

Para eliminar elementos del final de un array en JavaScript, puedes utilizar el método `Array.prototype.slice()`. Aquí te muestra cómo hacerlo:

```js
const takeRight = (arr, n = 1) => arr.slice(arr.length - n, arr.length);
```

Esta función crea un nuevo array con los últimos `n` elementos del array original. Aquí te muestra cómo puedes utilizarla:

```js
takeRight([1, 2, 3], 2); // [ 2, 3 ]
takeRight([1, 2, 3]); // [3]
```

Para utilizar esta función, abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
