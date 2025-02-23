# Cálculo de la Distancia Euclidiana

Para calcular la distancia entre dos puntos en cualquier número de dimensiones, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Object.keys()` y `Array.prototype.map()` para mapear cada coordenada a su diferencia entre los dos puntos.
3. Utilice `Math.hypot()` para calcular la distancia euclidiana entre los dos puntos.

A continuación, se muestra un fragmento de código de ejemplo para ayudarlo a comenzar:

```js
const euclideanDistance = (a, b) =>
  Math.hypot(...Object.keys(a).map((k) => b[k] - a[k]));
```

Puede probar la función con estas entradas de muestra:

```js
euclideanDistance([1, 1], [2, 3]); // ~2.2361
euclideanDistance([1, 1, 1], [2, 3, 2]); // ~2.4495
```
