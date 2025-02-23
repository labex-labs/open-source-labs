# Transponer una matriz en JavaScript

Para transponer una matriz bidimensional en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.map()` para crear la transpuesta de la matriz bidimensional dada. El método `map()` crea una nueva matriz con los resultados de llamar a una función proporcionada en cada elemento de la matriz.
3. La función proporcionada debe tomar dos argumentos: el elemento actual de la matriz y su índice. En este caso, solo necesitamos el índice para crear la transpuesta.
4. Utilice el índice para acceder a los elementos correspondientes en cada fila de la matriz bidimensional y cree una nueva matriz con esos elementos. Esta será la nueva fila en la matriz transpuesta.
5. Repita el paso anterior para cada columna en la matriz bidimensional para crear la matriz transpuesta completa.

Aquí está el código para transponer una matriz bidimensional en JavaScript:

```js
const transpose = (arr) => arr[0].map((col, i) => arr.map((row) => row[i]));

transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]);
// [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
```
