# Calculando el percentil de coincidencias

Para calcular el percentil de coincidencias en la matriz dada a continuación o igual a un valor dado, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar la práctica de codificación.
2. Utilice el método `Array.prototype.reduce()` para calcular la cantidad de valores por debajo del valor dado y la cantidad de valores iguales al valor dado.
3. Aplique la fórmula del percentil para obtener el porcentaje de coincidencias.
4. Aquí hay un fragmento de código de ejemplo:

```js
const percentile = (arr, val) =>
  (100 *
    arr.reduce(
      (acc, v) => acc + (v < val ? 1 : 0) + (v === val ? 0.5 : 0),
      0
    )) /
  arr.length;
```

5. Para probar la función, use este código de ejemplo:

```js
percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6); // Salida: 55
```

Esta función devolverá el porcentaje de coincidencias en la matriz dada que son menores o iguales al valor dado.
