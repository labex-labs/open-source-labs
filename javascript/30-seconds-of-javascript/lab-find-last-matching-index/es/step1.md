# Cómo encontrar el índice del último elemento que coincide en una matriz utilizando JavaScript

Para encontrar el índice del último elemento que coincide con una cierta condición en una matriz de JavaScript, utiliza la función `findLastIndex`. Aquí está cómo se utiliza:

```js
const findLastIndex = (arr, fn) =>
  (arr
    .map((val, i) => [i, val])
    .filter(([i, val]) => fn(val, i, arr))
    .pop() || [-1])[0];
```

La función `findLastIndex` toma dos argumentos: la matriz en la que buscar y una función para probar cada elemento. Aquí está cómo funciona:

1. Utiliza `Array.prototype.map()` para crear una nueva matriz de pares `[índice, valor]`.
2. Utiliza `Array.prototype.filter()` para eliminar los elementos de la matriz que no coinciden con la condición proporcionada por la función `fn`.
3. Utiliza `Array.prototype.pop()` para obtener el último elemento de la matriz filtrada.
4. Si la matriz filtrada está vacía, devuelve `-1`.

Aquí hay un ejemplo de cómo utilizar `findLastIndex`:

```js
findLastIndex([1, 2, 3, 4], (n) => n % 2 === 1); // 2 (índice del valor 3)
findLastIndex([1, 2, 3, 4], (n) => n === 5); // -1 (valor predeterminado cuando no se encuentra)
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
