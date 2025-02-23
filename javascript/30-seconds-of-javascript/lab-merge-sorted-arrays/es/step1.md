# Instrucciones para fusionar matrices ordenadas en JavaScript

Para fusionar dos matrices ordenadas en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el operador de propagación (`...`) para clonar ambas matrices dadas.
3. Utilice `Array.from()` para crear una matriz de la longitud adecuada basada en las matrices dadas.
4. Utilice `Array.prototype.shift()` para poblar la matriz recién creada a partir de los elementos eliminados de las matrices clonadas.

A continuación, se muestra un fragmento de código de ejemplo para fusionar dos matrices ordenadas:

```js
const mergeSortedArrays = (a, b) => {
  const _a = [...a],
    _b = [...b];
  return Array.from({ length: _a.length + _b.length }, () => {
    if (!_a.length) return _b.shift();
    else if (!_b.length) return _a.shift();
    else return _a[0] > _b[0] ? _b.shift() : _a.shift();
  });
};

console.log(mergeSortedArrays([1, 4, 5], [2, 3, 6])); // Output: [1, 2, 3, 4, 5, 6]
```

En el código anterior, la función `mergeSortedArrays` toma dos matrices ordenadas como argumentos y devuelve la matriz fusionada siguiendo los pasos anteriores. La salida del código de ejemplo es `[1, 2, 3, 4, 5, 6]`.
