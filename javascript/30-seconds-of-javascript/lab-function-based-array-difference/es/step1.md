# Cómo filtrar valores de un array basados en una función

Para filtrar todos los valores de un array basados en una función comparadora dada, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.filter()` y `Array.prototype.findIndex()` para encontrar los valores adecuados.
3. Omita el último argumento, `comp`, para utilizar un comparador de igualdad estricta predeterminado.
4. Utilice el siguiente código:

```js
const differenceWith = (arr, val, comp = (a, b) => a === b) =>
  arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1);
```

5. Pruebe su función con los siguientes ejemplos:

```js
differenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0],
  (a, b) => Math.round(a) === Math.round(b)
); // Salida esperada: [1, 1.2]

differenceWith([1, 1.2, 1.3], [1, 1.3, 1.5]); // Salida esperada: [1.2]
```
