# Comment filtrer des valeurs à partir d'un tableau en fonction d'une fonction

Pour filtrer toutes les valeurs d'un tableau en fonction d'une fonction de comparaison donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.filter()` et `Array.prototype.findIndex()` pour trouver les valeurs appropriées.
3. Omettez le dernier argument, `comp`, pour utiliser un comparateur d'égalité stricte par défaut.
4. Utilisez le code suivant :

```js
const differenceWith = (arr, val, comp = (a, b) => a === b) =>
  arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1);
```

5. Testez votre fonction avec les exemples suivants :

```js
differenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0],
  (a, b) => Math.round(a) === Math.round(b)
); // Sortie attendue : [1, 1.2]

differenceWith([1, 1.2, 1.3], [1, 1.3, 1.5]); // Sortie attendue : [1.2]
```
