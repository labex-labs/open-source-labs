# Generando una matriz de enteros aleatorios en un rango específico

Para generar una matriz de enteros aleatorios en un rango específico, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.from()` para crear una matriz vacía de la longitud deseada.
3. Utilice `Math.random()` para generar números aleatorios y mapearlos al rango especificado. Utilice `Math.floor()` para convertirlos en enteros.
4. La función `randomIntArrayInRange()` toma tres argumentos: `min`, `max` y un argumento opcional `n` (valor predeterminado es 1).
5. Llame a la función `randomIntArrayInRange()` con los valores deseados de `min`, `max` y `n` para generar la matriz de enteros aleatorios.

Aquí está el código:

```js
const randomIntArrayInRange = (min, max, n = 1) =>
  Array.from(
    { length: n },
    () => Math.floor(Math.random() * (max - min + 1)) + min
  );
```

Uso de ejemplo:

```js
randomIntArrayInRange(12, 35, 10); // [ 34, 14, 27, 17, 30, 27, 20, 26, 21, 14 ]
```
