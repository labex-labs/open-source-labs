# Implementierung des k-Means-Clustering-Algorithmus in JavaScript

Um zu beginnen, die Programmierung mit dem k-Means-Clustering-Algorithmus zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dieser Algorithmus gruppiert die gegebenen Daten in `k` Cluster, indem er den [k-Means-Clustering](https://en.wikipedia.org/wiki/K-means_clustering)-Algorithmus anwendet.

Die folgenden Schritte werden bei der Implementierung verwendet:

1. Initialisieren Sie geeignete Variablen für die Clusterzentren (`centroids`), die Distanzen (`distances`) und die Klassen (`classes`) mit `Array.from()` und `Array.prototype.slice()`.
2. Wiederholen Sie die Zuweisungs- und Aktualisierungsschritte mit einer `while`-Schleife, solange es in der vorherigen Iteration Änderungen gibt, wie dies durch `itr` angegeben ist.
3. Berechnen Sie die euklidische Distanz zwischen jedem Datenpunkt und dem Zentrum mit `Math.hypot()`, `Object.keys()` und `Array.prototype.map()`.
4. Finden Sie das nächste Zentrum mit `Array.prototype.indexOf()` und `Math.min()`.
5. Berechnen Sie die neuen Zentrum mit `Array.from()`, `Array.prototype.reduce()`, `parseFloat()` und `Number.prototype.toFixed()`.

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

Um den Algorithmus zu testen, rufen Sie die `kMeans()`-Funktion mit einem Datenarray und der gewünschten Anzahl von Clustern `k` auf. Die Funktion gibt ein Array von Klassenzuweisungen für jeden Datenpunkt zurück.

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
