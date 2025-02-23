# Algorithme de tri par tas

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez 'node'. L'algorithme suivant trie un tableau de nombres en utilisant l'algorithme de tri par tas. Suivez ces étapes :

- Utilisez la récursivité dans la fonction.
- Utilisez l'opérateur de propagation `(...)` pour cloner le tableau original, `arr`.
- Utilisez des fermetures pour déclarer une variable, `l`, et une fonction `heapify`.
- Utilisez une boucle `for` et `Math.floor()` en combinaison avec `heapify` pour créer un tas maximal à partir du tableau.
- Utilisez une boucle `for` pour réduire progressivement la plage considérée, en utilisant `heapify` et en échangeant les valeurs si nécessaire pour trier le tableau cloné.

```js
const heapsort = (arr) => {
  const a = [...arr];
  let l = a.length;
  const heapify = (a, i) => {
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    let max = i;
    if (left < l && a[left] > a[max]) max = left;
    if (right < l && a[right] > a[max]) max = right;
    if (max !== i) {
      [a[max], a[i]] = [a[i], a[max]];
      heapify(a, max);
    }
  };
  for (let i = Math.floor(l / 2); i >= 0; i -= 1) heapify(a, i);
  for (let i = a.length - 1; i > 0; i--) {
    [a[0], a[i]] = [a[i], a[0]];
    l--;
    heapify(a, 0);
  }
  return a;
};
```

Par exemple :

```js
heapsort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
