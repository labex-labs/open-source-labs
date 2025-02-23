# Algoritmo de clasificación por cubetas (Bucket Sort)

Para utilizar el algoritmo de clasificación por cubetas y ordenar una matriz de números, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Encuentre los valores mínimo y máximo de la matriz dada utilizando `Math.min()`, `Math.max()` y el operador de propagación (`...`).
3. Cree la cantidad adecuada de `cubetas` (matrices vacías) utilizando `Array.from()` y `Math.floor()`.
4. Rellene cada cubeta con los elementos adecuados de la matriz utilizando `Array.prototype.forEach()`.
5. Ordene cada cubeta y agréguela al resultado utilizando `Array.prototype.reduce()`, el operador de propagación (`...`) y `Array.prototype.sort()`.

A continuación, se muestra una implementación de ejemplo del algoritmo de clasificación por cubetas en JavaScript:

```js
const bucketSort = (arr, size = 5) => {
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const buckets = Array.from(
    { length: Math.floor((max - min) / size) + 1 },
    () => []
  );
  arr.forEach((val) => {
    buckets[Math.floor((val - min) / size)].push(val);
  });
  return buckets.reduce((acc, b) => [...acc, ...b.sort((a, b) => a - b)], []);
};
```

Para probar el algoritmo, ejecute el siguiente código:

```js
bucketSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
