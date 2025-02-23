# Instrucciones para calcular el punto medio entre dos pares de puntos (x,y):

Para calcular el punto medio entre dos pares de puntos (x,y), siga estos pasos:

1. Desestructura el array para obtener `x1`, `y1`, `x2` e `y2`.
2. Calcula el punto medio para cada dimensión dividiendo la suma de los dos extremos por `2`.

A continuación, se muestra un fragmento de código de ejemplo que implementa la función de cálculo del punto medio:

```js
const midpoint = ([x1, y1], [x2, y2]) => [(x1 + x2) / 2, (y1 + y2) / 2];
```

Puedes llamar a la función `midpoint` con los siguientes parámetros para obtener las coordenadas del punto medio:

```js
midpoint([2, 2], [4, 4]); // [3, 3]
midpoint([4, 4], [6, 6]); // [5, 5]
midpoint([1, 3], [2, 4]); // [1.5, 3.5]
```

# Primeros pasos en la codificación:

Para comenzar a practicar la codificación, siga estos pasos:

1. Abre la Terminal/SSH.
2. Escribe `node` para iniciar el entorno de Node.js.
