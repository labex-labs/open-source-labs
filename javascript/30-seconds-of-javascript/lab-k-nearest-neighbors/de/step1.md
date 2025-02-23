# K-Nearest-Neighbors-Algorithmus

Um den K-Nearest-Neighbors-Algorithmus zu verwenden, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein.
2. Klassifizieren Sie einen Datenpunkt relativ zu einem markierten Datensatz mit dem [k-nearest neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)-Algorithmus.
3. Abbilden Sie die `data` auf Objekte mit `Array.prototype.map()`. Jedes Objekt enthält die euklidische Entfernung des Elements von `point`, berechnet mit `Math.hypot()`, `Object.keys()` und seinem `label`.
4. Verwenden Sie `Array.prototype.sort()` und `Array.prototype.slice()`, um die `k` nächsten Nachbarn von `point` zu erhalten.
5. Verwenden Sie `Array.prototype.reduce()` in Kombination mit `Object.keys()` und `Array.prototype.indexOf()`, um das am häufigsten vorkommende `label` unter ihnen zu finden.

Hier ist ein Beispielcode, der den K-Nearest-Neighbors-Algorithmus implementiert:

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

So verwenden Sie den Code:

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
