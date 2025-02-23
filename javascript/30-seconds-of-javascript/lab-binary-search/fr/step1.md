# Algorithme de recherche dichotomique

Pour commencer la pratique de codage, ouvrez le Terminal/SSH et tapez `node`. L'algorithme de recherche dichotomique est utilisé pour trouver l'index d'un élément donné dans un tableau trié. Voici les étapes pour implémenter l'algorithme de recherche dichotomique :

1. Décarez les limites de recherche gauche et droite, `l` et `r`, initialisées à `0` et à la `longueur` du tableau respectivement.
2. Utilisez une boucle `while` pour réduire progressivement le sous-tableau de recherche en le divisant par deux à l'aide de `Math.floor()`.
3. Si l'élément est trouvé, renvoyez son index. Sinon, renvoyez `-1`.
4. Notez que cet algorithme ne prend pas en compte les valeurs dupliquées dans le tableau.

Voici une implémentation exemple de l'algorithme de recherche dichotomique en JavaScript :

```js
const binarySearch = (arr, item) => {
  let l = 0,
    r = arr.length - 1;
  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    const guess = arr[mid];
    if (guess === item) return mid;
    if (guess > item) r = mid - 1;
    else l = mid + 1;
  }
  return -1;
};
```

Vous pouvez tester la fonction `binarySearch` avec les exemples suivants :

```js
binarySearch([1, 2, 3, 4, 5], 1); // 0
binarySearch([1, 2, 3, 4, 5], 5); // 4
binarySearch([1, 2, 3, 4, 5], 6); // -1
```
