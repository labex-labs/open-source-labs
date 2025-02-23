# Calculando la Distancia Entre Dos Puntos

Para calcular la distancia entre dos puntos, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Math.hypot()` para calcular la distancia euclidiana entre dos puntos.
3. Implementa el código siguiente, reemplazando los valores de `x0`, `y0`, `x1` e `y1` con las coordenadas de tus puntos.

```js
const distance = (x0, y0, x1, y1) => Math.hypot(x1 - x0, y1 - y0);
```

Aquí hay un ejemplo de cómo utilizar esta función:

```js
distance(1, 1, 2, 3); // ~2.2361
```

Esto devolverá la distancia entre los puntos `(1, 1)` y `(2, 3)`.
