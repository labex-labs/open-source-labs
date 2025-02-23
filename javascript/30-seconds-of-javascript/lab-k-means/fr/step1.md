# Implémentation de l'algorithme de clustering k-means en JavaScript

Pour commencer à pratiquer la programmation en utilisant l'algorithme de clustering k-means, ouvrez le Terminal/SSH et tapez `node`. Cet algorithme regroupe les données données en `k` clusters, en utilisant l'algorithme de [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering).

Les étapes suivantes sont utilisées dans l'implémentation :

1. Initialisez des variables appropriées pour les centroïdes de cluster, les distances et les classes à l'aide de `Array.from()` et `Array.prototype.slice()`.
2. Répétez les étapes d'attribution et de mise à jour à l'aide d'une boucle `while` tant qu'il y a des changements dans l'itération précédente, comme indiqué par `itr`.
3. Calculez la distance euclidienne entre chaque point de données et le centroïde à l'aide de `Math.hypot()`, `Object.keys()` et `Array.prototype.map()`.
4. Trouvez le centroïde le plus proche à l'aide de `Array.prototype.indexOf()` et `Math.min()`.
5. Calculez les nouveaux centroïdes à l'aide de `Array.from()`, `Array.prototype.reduce()`, `parseFloat()` et `Number.prototype.toFixed()`.

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

Pour tester l'algorithme, appelez la fonction `kMeans()` avec un tableau de données et le nombre de clusters `k` souhaité. La fonction renvoie un tableau d'attributions de classes pour chaque point de données.

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
