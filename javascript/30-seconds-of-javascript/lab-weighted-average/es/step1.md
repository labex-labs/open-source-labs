# Cómo calcular el promedio ponderado en JavaScript

Para calcular el promedio ponderado de dos o más números en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.reduce()` para crear la suma ponderada de los valores y la suma de los pesos.
3. Divide la suma ponderada de los valores entre la suma de los pesos para obtener el promedio ponderado.

Aquí está el código JavaScript para la función `weightedAverage`:

```js
const weightedAverage = (nums, weights) => {
  const [sum, weightSum] = weights.reduce(
    (acc, w, i) => {
      acc[0] = acc[0] + nums[i] * w;
      acc[1] = acc[1] + w;
      return acc;
    },
    [0, 0]
  );
  return sum / weightSum;
};
```

Puedes utilizar la función `weightedAverage` para calcular el promedio ponderado de una matriz de números y una matriz de pesos de la siguiente manera:

```js
weightedAverage([1, 2, 3], [0.6, 0.2, 0.3]); // 1.72727
```
