# Una función para encontrar la coincidencia numérica más cercana en una matriz

Para encontrar el número más cercano en una matriz, utiliza la siguiente función:

```js
const closest = (arr, n) =>
  arr.reduce((acc, num) => (Math.abs(num - n) < Math.abs(acc - n) ? num : acc));
```

Aquí está cómo utilizarla:

1. Abre la Terminal/SSH.
2. Escribe `node`.
3. Utiliza la función `closest()` y proporciona la matriz y el valor objetivo como argumentos.

Uso de ejemplo: `closest([6, 1, 3, 7, 9], 5)` devolverá `6`, que es el número más cercano a `5` en la matriz.
