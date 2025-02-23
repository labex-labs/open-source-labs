# Filtrado de valores no únicos de una matriz con una función

Para comenzar a practicar la codificación, abra la Terminal/SSH y escriba `node`.

Este código filtra los valores no únicos de una matriz, en función de una función comparadora proporcionada. Estos son los pasos para lograr esto:

1. Utilice `Array.prototype.filter()` y `Array.prototype.every()` para crear una nueva matriz con solo los valores únicos en función de la función comparadora `fn`.
2. La función comparadora toma cuatro argumentos: los valores de los dos elementos que se están comparando y sus índices.
3. La función `filterNonUniqueBy` implementa los pasos anteriores y devuelve la matriz de valores únicos.

```js
const filterNonUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.every((x, j) => (i === j) === fn(v, x, i, j)));
```

Este es un ejemplo de cómo utilizar esta función:

```js
filterNonUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id === b.id
); // [ { id: 2, value: 'c' } ]
```

Este código es conciso, claro y coherente y debería funcionar como se espera.
