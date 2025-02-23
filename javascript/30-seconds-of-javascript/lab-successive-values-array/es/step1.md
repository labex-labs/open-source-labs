# Matriz de valores sucesivos

Para crear una matriz de valores sucesivos en JavaScript, puedes usar el método `Array.prototype.reduce()`. Este método aplica una función a un acumulador y cada elemento de la matriz, de izquierda a derecha, y devuelve una matriz de los valores reducidos sucesivamente.

Aquí está cómo usar la función `reduceSuccessive` para aplicar la función dada a la matriz dada, almacenando cada nuevo resultado:

```js
const reduceSuccessive = (arr, fn, acc) =>
  arr.reduce(
    (res, val, i, arr) => (res.push(fn(res.slice(-1)[0], val, i, arr)), res),
    [acc]
  );
```

Luego, puedes llamar a la función `reduceSuccessive` con una matriz, una función y un valor inicial para el acumulador:

```js
reduceSuccessive([1, 2, 3, 4, 5, 6], (acc, val) => acc + val, 0);
// [0, 1, 3, 6, 10, 15, 21]
```

Para comenzar a practicar la codificación con esta función, abre la Terminal/SSH y escribe `node`.
