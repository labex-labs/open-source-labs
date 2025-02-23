# Función para inicializar una matriz con valores especificados

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Esta función inicializa una matriz con los valores especificados:

- Utiliza el constructor `Array()` para crear una matriz de la longitud deseada.
- Utiliza `Array.prototype.fill()` para llenarla con los valores deseados.
- Si no se especifica ningún valor, el valor predeterminado es `0`.

```js
const initializeArrayWithValues = (length, value = 0) =>
  Array(length).fill(value);
```

Uso de ejemplo:

```js
initializeArrayWithValues(5, 2); // [2, 2, 2, 2, 2]
```
