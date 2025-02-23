# Práctica de código: Comprobar si una matriz está ordenada

Para practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí hay una función para comprobar si una matriz numérica está ordenada:

```js
const isSorted = (arr) => {
  if (arr.length <= 1) return 0;
  const direction = arr[1] - arr[0];
  for (let i = 2; i < arr.length; i++) {
    if ((arr[i] - arr[i - 1]) * direction < 0) return 0;
  }
  return Math.sign(direction);
};
```

Para utilizarla, pasa una matriz de números a `isSorted()`. La función devolverá `1` si la matriz está ordenada en orden ascendente, `-1` si está ordenada en orden descendente y `0` si no está ordenada.

Aquí hay algunos ejemplos:

```js
isSorted([0, 1, 2, 2]); // 1
isSorted([4, 3, 2]); // -1
isSorted([4, 3, 5]); // 0
isSorted([4]); // 0
```
