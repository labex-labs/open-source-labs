# Algorithme de tri Fusion

Pour pratiquer la programmation en utilisant l'algorithme de tri Fusion, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node`.
2. Utilisez la récursivité pour trier un tableau de nombres.
3. Si la `longueur` du tableau est inférieure à `2`, renvoyez le tableau.
4. Utilisez `Math.floor()` pour calculer le point milieu du tableau.
5. Utilisez `Array.prototype.slice()` pour couper le tableau en deux et appelez récursivement `mergeSort()` sur les sous-tableaux créés.
6. Enfin, utilisez `Array.from()` et `Array.prototype.shift()` pour combiner les deux sous-tableaux triés en un seul.

Voici le code :

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

Essayez-le avec cet exemple :

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
