# Cómo inicializar una matriz de N dimensiones en JavaScript

Para crear una matriz de N dimensiones en JavaScript, puedes utilizar la función `initializeNDArray`. Esta función toma un valor y cualquier número de dimensiones como argumentos y devuelve una nueva matriz inicializada con ese valor.

Para utilizar `initializeNDArray`, puedes seguir estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a codificar.
2. Utiliza la recursividad para crear la matriz con el número dado de dimensiones.
3. Utiliza `Array.from()` y `Array.prototype.map()` para generar filas donde cada fila es una nueva matriz inicializada utilizando `initializeNDArray()`.

Aquí está el código de la función `initializeNDArray`:

```js
const initializeNDArray = (val, ...args) =>
  args.length === 0
    ? val
    : Array.from({ length: args[0] }).map(() =>
        initializeNDArray(val, ...args.slice(1))
      );
```

Luego puedes llamar a `initializeNDArray` con el valor y el número de dimensiones deseados. Por ejemplo:

```js
initializeNDArray(1, 3); // [1, 1, 1]
initializeNDArray(5, 2, 2, 2); // [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
```
