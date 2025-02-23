# Algorithme de tri rapide

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Cet algorithme trie un tableau de nombres en utilisant l'algorithme de tri rapide. Voici les étapes à suivre :

- Utiliser la récursivité.
- Utiliser l'opérateur de propagation (`...`) pour cloner le tableau original, `arr`.
- Si la `longueur` du tableau est inférieure à `2`, retourner le tableau cloné.
- Utiliser `Math.floor()` pour calculer l'index de l'élément pivot.
- Utiliser `Array.prototype.reduce()` et `Array.prototype.push()` pour diviser le tableau en deux sous-tableaux. Le premier contient les éléments plus petits ou égaux à `pivot`, et le second contient les éléments plus grands que lui. Découpez le résultat en deux tableaux.
- Appeler récursivement `quickSort()` sur les sous-tableaux créés.

Voici un exemple de mise en œuvre de cet algorithme :

```js
const quickSort = (arr) => {
  const a = [...arr];
  if (a.length < 2) return a;
  const pivotIndex = Math.floor(arr.length / 2);
  const pivot = a[pivotIndex];
  const [lo, hi] = a.reduce(
    (acc, val, i) => {
      if (val < pivot || (val === pivot && i != pivotIndex)) {
        acc[0].push(val);
      } else if (val > pivot) {
        acc[1].push(val);
      }
      return acc;
    },
    [[], []]
  );
  return [...quickSort(lo), pivot, ...quickSort(hi)];
};
```

Pour le tester, exécutez la commande suivante :

```js
quickSort([1, 6, 1, 5, 3, 2, 1, 4]); // [1, 1, 1, 2, 3, 4, 5, 6]
```
