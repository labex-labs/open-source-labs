# Algoritmo para particionar una matriz

Para particionar una matriz, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Aplique la función `fn` proporcionada a cada valor en la matriz `arr` dada.
3. Divida la matriz cada vez que `fn` devuelva un nuevo valor.
4. Utilice `Array.prototype.reduce()` para crear un objeto acumulador que contenga la matriz resultante y el último valor devuelto por `fn`.
5. Utilice `Array.prototype.push()` para agregar cada valor en `arr` a la partición adecuada en la matriz acumulador.
6. Devuelva la matriz resultante.

A continuación, se muestra la implementación del código:

```js
const partitionBy = (arr, fn) =>
  arr.reduce(
    ({ res, last }, v, i, a) => {
      const next = fn(v, i, a);
      if (next !== last) res.push([v]);
      else res[res.length - 1].push(v);
      return { res, last: next };
    },
    { res: [] }
  ).res;
```

Uso de ejemplo:

```js
const numbers = [1, 1, 3, 3, 4, 5, 5, 5];
partitionBy(numbers, (n) => n % 2 === 0); // [[1, 1, 3, 3], [4], [5, 5, 5]]
partitionBy(numbers, (n) => n); // [[1, 1], [3, 3], [4], [5, 5, 5]]
```
