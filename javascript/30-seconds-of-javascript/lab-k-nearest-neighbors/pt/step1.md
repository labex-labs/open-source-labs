# Algoritmo K-Nearest Neighbors

Para usar o Algoritmo K-Nearest Neighbors, siga estes passos:

1.  Abra o Terminal/SSH e digite `node`.
2.  Classifique um ponto de dados em relação a um conjunto de dados rotulados usando o algoritmo [k-nearest neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm).
3.  Mapeie os `data` para objetos usando `Array.prototype.map()`. Cada objeto contém a distância Euclidiana do elemento a partir de `point`, calculada usando `Math.hypot()`, `Object.keys()` e seu `label`.
4.  Use `Array.prototype.sort()` e `Array.prototype.slice()` para obter os `k` vizinhos mais próximos de `point`.
5.  Use `Array.prototype.reduce()` em combinação com `Object.keys()` e `Array.prototype.indexOf()` para encontrar o `label` mais frequente entre eles.

Aqui está um exemplo de código que implementa o Algoritmo K-Nearest Neighbors:

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

Veja como usar o código:

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
