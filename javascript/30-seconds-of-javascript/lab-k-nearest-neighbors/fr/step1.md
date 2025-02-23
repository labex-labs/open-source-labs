# Algorithme des K Plus Proches Voisins

Pour utiliser l'algorithme des K Plus Proches Voisins, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node`.
2. Classifiez un point de données par rapport à un ensemble de données étiquetées à l'aide de l'algorithme des [k plus proches voisins](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm).
3. Appliquez la méthode `Array.prototype.map()` sur les `data` pour les convertir en objets. Chaque objet contient la distance euclidienne de l'élément à partir de `point`, calculée à l'aide de `Math.hypot()`, `Object.keys()` et son `label`.
4. Utilisez `Array.prototype.sort()` et `Array.prototype.slice()` pour obtenir les `k` plus proches voisins de `point`.
5. Utilisez `Array.prototype.reduce()` en combinaison avec `Object.keys()` et `Array.prototype.indexOf()` pour trouver le `label` le plus fréquent parmi eux.

Voici un exemple de code qui implémente l'algorithme des K Plus Proches Voisins :

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

Voici comment utiliser le code :

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
