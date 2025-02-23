# Inicializar una matriz mapeada en JavaScript

Para inicializar una matriz mapeada en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el constructor `Array()` para crear una matriz de la longitud deseada.
3. Utilice `Array.prototype.fill()` para llenar la matriz con valores `null`.
4. Utilice `Array.prototype.map()` para llenar la matriz con los valores deseados, utilizando la función proporcionada, `mapFn`.
5. Omita el segundo argumento, `mapFn`, para mapear cada elemento a su índice.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const initializeMappedArray = (n, mapFn = (_, i) => i) =>
  Array(n).fill(null).map(mapFn);
```

Puede utilizar la función `initializeMappedArray` para crear una matriz mapeada con los valores deseados:

```js
initializeMappedArray(5); // [0, 1, 2, 3, 4]
initializeMappedArray(5, (i) => `item ${i + 1}`);
// ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
```
