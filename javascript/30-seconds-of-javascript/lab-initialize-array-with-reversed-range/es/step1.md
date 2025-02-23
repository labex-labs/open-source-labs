# Cómo inicializar una matriz con un rango invertido en JavaScript

Para inicializar una matriz con un rango invertido en JavaScript, utiliza la siguiente función:

```js
const initializeArrayWithRangeRight = (end, start = 0, step = 1) =>
  Array.from({ length: Math.ceil((end + 1 - start) / step) }).map(
    (v, i, arr) => (arr.length - i - 1) * step + start
  );
```

Esta función crea una matriz que contiene los números en el rango especificado en orden inverso. Los parámetros `start` y `end` son inclusivos, y el parámetro `step` especifica la diferencia común entre los números en el rango.

Para utilizar la función, llámala con los valores deseados de `end`, `start` y `step` como argumentos, así:

```js
initializeArrayWithRangeRight(5); // [5, 4, 3, 2, 1, 0]
initializeArrayWithRangeRight(7, 3); // [7, 6, 5, 4, 3]
initializeArrayWithRangeRight(9, 0, 2); // [8, 6, 4, 2, 0]
```

Si omites el argumento `start`, el valor predeterminado es `0`. Si omites el argumento `step`, el valor predeterminado es `1`.
