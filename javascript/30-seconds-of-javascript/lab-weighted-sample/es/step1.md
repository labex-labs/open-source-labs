# Cómo obtener una muestra ponderada de una matriz en JavaScript

Para obtener aleatoriamente un elemento de una matriz según los pesos proporcionados, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.reduce()` para crear una matriz de sumas parciales para cada valor en `weights`.
3. Utilice `Math.random()` para generar un número aleatorio y `Array.prototype.findIndex()` para encontrar el índice correcto basado en la matriz producida previamente.
4. Finalmente, devuelva el elemento de `arr` con el índice producido.

A continuación, se muestra el código para lograr esto:

```js
const weightedSample = (arr, weights) => {
  let roll = Math.random();
  return arr[
    weights
      .reduce(
        (acc, w, i) => (i === 0 ? [w] : [...acc, acc[acc.length - 1] + w]),
        []
      )
      .findIndex((v, i, s) => roll >= (i === 0 ? 0 : s[i - 1]) && roll < v)
  ];
};
```

Puede probar esta función pasando una matriz y sus pesos correspondientes como argumentos:

```js
weightedSample([3, 7, 9, 11], [0.1, 0.2, 0.6, 0.1]); // 9
```
