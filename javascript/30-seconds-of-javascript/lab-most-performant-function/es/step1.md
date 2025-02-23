# Cómo encontrar la función más eficiente en JavaScript

Para encontrar la función más eficiente en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.map()` para generar una matriz donde cada valor sea el tiempo total que tarda en ejecutarse la función después de `iteraciones` veces.
3. Utiliza la diferencia de los valores de `performance.now()` antes y después para obtener el tiempo total en milisegundos con un alto grado de precisión.
4. Utiliza `Math.min()` para encontrar el tiempo de ejecución mínimo y devuelve el índice de ese tiempo más corto que corresponde al índice de la función más eficiente.
5. Si omites el segundo argumento, `iteraciones`, la función utilizará un valor predeterminado de `10000` iteraciones.
6. Tien en cuenta que cuanto más iteraciones uses, más fiable será el resultado pero más tiempo tardará.

Aquí hay un fragmento de código de ejemplo:

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

Para utilizar esta función, pasa una matriz de funciones como primer argumento y el número de iteraciones como segundo argumento (opcional). Por ejemplo:

```js
mostPerformant([
  () => {
    // Recorre toda la matriz antes de devolver `false`
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // Solo necesita llegar al índice `1` antes de devolver `false`
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
