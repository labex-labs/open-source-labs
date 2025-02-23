# Implementación del algoritmo de agrupamiento k-means en JavaScript

Para comenzar a practicar la codificación utilizando el algoritmo de agrupamiento k-means, abre la Terminal/SSH y escribe `node`. Este algoritmo agrupa los datos dados en `k` clusters, utilizando el algoritmo de [agrupamiento k-means](https://en.wikipedia.org/wiki/K-means_clustering).

Los siguientes pasos se utilizan en la implementación:

1. Inicializa variables adecuadas para los centroides del cluster, las distancias y las clases utilizando `Array.from()` y `Array.prototype.slice()`.
2. Repite los pasos de asignación y actualización utilizando un bucle `while` mientras haya cambios en la iteración anterior, como se indica por `itr`.
3. Calcula la distancia euclidiana entre cada punto de datos y el centroide utilizando `Math.hypot()`, `Object.keys()` y `Array.prototype.map()`.
4. Encuentra el centroide más cercano utilizando `Array.prototype.indexOf()` y `Math.min()`.
5. Calcula los nuevos centroides utilizando `Array.from()`, `Array.prototype.reduce()`, `parseFloat()` y `Number.prototype.toFixed()`.

```js
const kMeans = (data, k = 1) => {
  const centroids = data.slice(0, k);
  const distances = Array.from({ length: data.length }, () =>
    Array.from({ length: k }, () => 0)
  );
  const classes = Array.from({ length: data.length }, () => -1);
  let itr = true;

  while (itr) {
    itr = false;

    for (let d in data) {
      for (let c = 0; c < k; c++) {
        distances[d][c] = Math.hypot(
          ...Object.keys(data[0]).map((key) => data[d][key] - centroids[c][key])
        );
      }
      const m = distances[d].indexOf(Math.min(...distances[d]));
      if (classes[d] !== m) itr = true;
      classes[d] = m;
    }

    for (let c = 0; c < k; c++) {
      centroids[c] = Array.from({ length: data[0].length }, () => 0);
      const size = data.reduce((acc, _, d) => {
        if (classes[d] === c) {
          acc++;
          for (let i in data[0]) centroids[c][i] += data[d][i];
        }
        return acc;
      }, 0);
      for (let i in data[0]) {
        centroids[c][i] = parseFloat(Number(centroids[c][i] / size).toFixed(2));
      }
    }
  }

  return classes;
};
```

Para probar el algoritmo, llama a la función `kMeans()` con una matriz de datos y el número deseado de clusters `k`. La función devuelve una matriz de asignaciones de clase para cada punto de datos.

```js
kMeans(
  [
    [0, 0],
    [0, 1],
    [1, 3],
    [2, 0]
  ],
  2
); // [0, 1, 1, 0]
```
