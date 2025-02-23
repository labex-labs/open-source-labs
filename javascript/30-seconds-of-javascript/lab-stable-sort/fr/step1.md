# Tri stable

Pour effectuer un tri stable d'un tableau et conserver les index initiaux des éléments ayant les mêmes valeurs, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.map()` pour associer chaque élément du tableau d'entrée à son index correspondant.
3. Utilisez `Array.prototype.sort()` avec une fonction `compare` pour trier la liste tout en conservant l'ordre initial si les éléments comparés sont égaux.
4. Utilisez `Array.prototype.map()` à nouveau pour convertir les éléments du tableau en leur forme initiale.
5. Le tableau original n'est pas modifié, et un nouveau tableau est renvoyé à la place.

Voici une implémentation de la fonction `stableSort` en JavaScript :

```js
const stableSort = (arr, compare) =>
  arr
    .map((item, index) => ({ item, index }))
    .sort((a, b) => compare(a.item, b.item) || a.index - b.index)
    .map(({ item }) => item);
```

Vous pouvez appeler la fonction `stableSort` avec un tableau et une fonction `compare` pour obtenir un nouveau tableau avec les éléments triés, comme indiqué ci-dessous :

```js
const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const stable = stableSort(arr, () => 0); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
