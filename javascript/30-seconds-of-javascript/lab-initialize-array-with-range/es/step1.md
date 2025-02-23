# Función para inicializar un array con un rango

Para inicializar un array con un rango de números, utiliza la siguiente función:

```js
const initializeArrayWithRange = (end, start = 0, step = 1) => {
  const length = Math.ceil((end - start + 1) / step);
  return Array.from({ length }, (_, i) => i * step + start);
};
```

Esta función toma tres argumentos: `end` (requerido), `start` (opcional, valor predeterminado es `0`) y `step` (opcional, valor predeterminado es `1`). Devuelve un array que contiene los números en el rango especificado, donde `start` y `end` son inclusivos con su diferencia común `step`.

Para utilizar esta función, simplemente llámala con los parámetros de rango deseados:

```js
initializeArrayWithRange(5); // [0, 1, 2, 3, 4, 5]
initializeArrayWithRange(7, 3); // [3, 4, 5, 6, 7]
initializeArrayWithRange(9, 0, 2); // [0, 2, 4, 6, 8]
```

Esta función utiliza `Array.from()` para crear un array de la longitud deseada, y luego una función `map` para llenar el array con los valores deseados en el rango dado. Si omites el segundo argumento, `start`, utilizará un valor predeterminado de `0`. Si omites el último argumento, `step`, utilizará un valor predeterminado de `1`.
