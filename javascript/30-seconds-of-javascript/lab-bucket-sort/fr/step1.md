# Algorithme de tri par bac

Pour utiliser l'algorithme de tri par bac et trier un tableau de nombres, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Trouvez les valeurs minimale et maximale du tableau donné en utilisant `Math.min()`, `Math.max()` et l'opérateur de propagation (`...`).
3. Créez le nombre approprié de `bac` (tableaux vides) en utilisant `Array.from()` et `Math.floor()`.
4. Remplissez chaque bac avec les éléments appropriés du tableau en utilisant `Array.prototype.forEach()`.
5. Triez chaque bac et ajoutez-le au résultat en utilisant `Array.prototype.reduce()`, l'opérateur de propagation (`...`) et `Array.prototype.sort()`.

Voici une implémentation exemple de l'algorithme de tri par bac en JavaScript :

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

Pour tester l'algorithme, exécutez le code suivant :

```js
bucketSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
