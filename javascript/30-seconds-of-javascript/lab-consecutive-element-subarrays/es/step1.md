# Subarreglos de Elementos Consecutivos

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. El siguiente código crea una matriz de n-tuplas de elementos consecutivos.

```js
const aperture = (n, arr) =>
  n > arr.length ? [] : arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

Para utilizar la función:

- Llama a la función `aperture(n, arr)` con `n` como el número de elementos consecutivos y `arr` como la matriz de números.
- La función devuelve una matriz de n-tuplas de elementos consecutivos de `arr`.
- Si `n` es mayor que la longitud de `arr`, la función devuelve una matriz vacía.

Uso de ejemplo:

```js
aperture(2, [1, 2, 3, 4]); // [[1, 2], [2, 3], [3, 4]]
aperture(3, [1, 2, 3, 4]); // [[1, 2, 3], [2, 3, 4]]
aperture(5, [1, 2, 3, 4]); // []
```
