# Una función para encontrar la diferencia simétrica de arrays

Para encontrar la diferencia simétrica entre dos arrays utilizando una función proporcionada como comparador, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice los métodos `Array.prototype.filter()` y `Array.prototype.findIndex()` para encontrar los valores adecuados.
3. Utilice el código dado para realizar la operación.

```js
const symmetricDifferenceWith = (arr, val, comp) => [
  ...arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1),
  ...val.filter((a) => arr.findIndex((b) => comp(a, b)) === -1)
];
```

Por ejemplo, considere la siguiente entrada:

```js
symmetricDifferenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
); // [1, 1.2, 3.9]
```

El código anterior devolverá `[1, 1.2, 3.9]` como la diferencia simétrica entre los dos arrays.
