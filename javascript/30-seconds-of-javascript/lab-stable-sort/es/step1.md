# Clasificación estable

Para realizar la clasificación estable de una matriz y conservar los índices iniciales de los elementos con valores iguales, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.map()` para emparejar cada elemento de la matriz de entrada con su índice correspondiente.
3. Utilice `Array.prototype.sort()` junto con una función `compare` para ordenar la lista mientras se conserva el orden inicial si los elementos comparados son iguales.
4. Utilice `Array.prototype.map()` nuevamente para convertir los elementos de la matriz de vuelta a su forma inicial.
5. La matriz original no se modifica, en su lugar se devuelve una nueva matriz.

A continuación, se muestra una implementación de la función `stableSort` en JavaScript:

```js
const stableSort = (arr, compare) =>
  arr
    .map((item, index) => ({ item, index }))
    .sort((a, b) => compare(a.item, b.item) || a.index - b.index)
    .map(({ item }) => item);
```

Puede llamar a la función `stableSort` con una matriz y una función `compare` para obtener una nueva matriz con los elementos ordenados, como se muestra a continuación:

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const stable = stableSort(arr, () => 0); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
