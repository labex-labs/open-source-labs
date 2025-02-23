# Algoritmo de K Vecinos más Cercanos

Para utilizar el Algoritmo de K Vecinos más Cercanos, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node`.
2. Clasifique un punto de datos con respecto a un conjunto de datos etiquetados utilizando el algoritmo de [k vecinos más cercanos](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm).
3. Asocie los `datos` a objetos utilizando `Array.prototype.map()`. Cada objeto contiene la distancia euclidiana del elemento desde `punto`, calculada utilizando `Math.hypot()`, `Object.keys()` y su `etiqueta`.
4. Utilice `Array.prototype.sort()` y `Array.prototype.slice()` para obtener los `k` vecinos más cercanos de `punto`.
5. Utilice `Array.prototype.reduce()` en combinación con `Object.keys()` y `Array.prototype.indexOf()` para encontrar la `etiqueta` más frecuente entre ellos.

A continuación, se muestra un código de ejemplo que implementa el Algoritmo de K Vecinos más Cercanos:

```js
const kNearestNeighbors = (data, labels, point, k = 3) => {
  const kNearest = data
    .map((el, i) => ({
      dist: Math.hypot(...Object.keys(el).map((key) => point[key] - el[key])),
      label: labels[i]
    }))
    .sort((a, b) => a.dist - b.dist)
    .slice(0, k);

  return kNearest.reduce(
    (acc, { label }, i) => {
      acc.classCounts[label] =
        Object.keys(acc.classCounts).indexOf(label) !== -1
          ? acc.classCounts[label] + 1
          : 1;
      if (acc.classCounts[label] > acc.topClassCount) {
        acc.topClassCount = acc.classCounts[label];
        acc.topClass = label;
      }
      return acc;
    },
    {
      classCounts: {},
      topClass: kNearest[0].label,
      topClassCount: 0
    }
  ).topClass;
};
```

A continuación, se muestra cómo utilizar el código:

```js
const data = [
  [0, 0],
  [0, 1],
  [1, 3],
  [2, 0]
];
const labels = [0, 1, 1, 0];

kNearestNeighbors(data, labels, [1, 2], 2); // 1
kNearestNeighbors(data, labels, [1, 0], 2); // 0
```
