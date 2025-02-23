# Encontrando el Énésimo Elemento de un Array

Para encontrar el enésimo elemento de un array, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.slice()` para crear un nuevo array que contenga el enésimo elemento.
3. Si el índice está fuera de los límites, devuelva `undefined`.
4. Omita el segundo argumento, `n`, para obtener el primer elemento del array.

A continuación, se muestra un código de ejemplo que implementa esto:

```js
const nthElement = (arr, n = 0) =>
  (n === -1 ? arr.slice(n) : arr.slice(n, n + 1))[0];
```

Puede probar esta función con los siguientes ejemplos:

```js
nthElement(["a", "b", "c"], 1); // Salida: 'b'
nthElement(["a", "b", "b"], -3); // Salida: 'a'
```

Siguiendo estos pasos, puede encontrar fácilmente el enésimo elemento de un array utilizando JavaScript.
