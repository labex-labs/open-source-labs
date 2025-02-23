# Comment générer toutes les permutations d'un tableau

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici un algorithme qui génère toutes les permutations des éléments d'un tableau (même s'il contient des doublons). Suivez ces étapes pour l'implémenter :

1. Utilisez la récursivité.
2. Pour chaque élément du tableau donné, créez toutes les permutations partielles des autres éléments.
3. Utilisez `Array.prototype.map()` pour combiner l'élément avec chaque permutation partielle, puis `Array.prototype.reduce()` pour combiner toutes les permutations en un seul tableau.
4. Les cas de base sont pour les tableaux de longueur `2` ou `1`.
5. Attention, le temps d'exécution de cette fonction augmente exponentiellement avec chaque élément du tableau. Plus de 8 à 10 entrées peuvent entraîner la suspension de votre navigateur car il essaye de résoudre toutes les combinaisons différentes.

Voici le code :

```js
const permutations = (arr) => {
  if (arr.length <= 2) return arr.length === 2 ? [arr, [arr[1], arr[0]]] : arr;
  return arr.reduce(
    (acc, item, i) =>
      acc.concat(
        permutations([...arr.slice(0, i), ...arr.slice(i + 1)]).map((val) => [
          item,
          ...val
        ])
      ),
    []
  );
};
```

Vous pouvez tester le code en appelant la fonction `permutations()` avec un argument de tableau :

```js
permutations([1, 33, 5]);
// [ [1, 33, 5], [1, 5, 33], [33, 1, 5], [33, 5, 1], [5, 1, 33], [5, 33, 1] ]
```
