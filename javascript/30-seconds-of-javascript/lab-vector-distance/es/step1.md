# Cálculo de la Distancia Vectorial

Para calcular la distancia entre dos vectores, sigue estos pasos:

1. Abre la Terminal/SSH para comenzar a practicar la codificación.
2. Escribe `node` para comenzar.
3. Utiliza `Array.prototype.reduce()`, `Math.pow()` y `Math.sqrt()` para encontrar la distancia euclidiana entre los vectores.
4. Aplica la fórmula `vectorDistance`, que se muestra a continuación:

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5. Prueba la fórmula ingresando dos vectores en el siguiente formato: `vectorDistance([10, 0, 5], [20, 0, 10]);`
6. La salida será la distancia entre los dos vectores: `11.180339887498949`.
