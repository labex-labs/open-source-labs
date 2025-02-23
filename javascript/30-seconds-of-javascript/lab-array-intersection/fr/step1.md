# Trouver l'intersection d'ensembles

Pour trouver les éléments communs entre deux tableaux et éliminer les doublons, utilisez le code suivant :

```js
const intersection = (arr1, arr2) => {
  const set = new Set(arr2);
  return [...new Set(arr1)].filter((elem) => set.has(elem));
};
```

Pour utiliser ce code, ouvrez le Terminal/SSH et tapez `node`. Ensuite, appelez la fonction `intersection` avec deux tableaux en tant qu'arguments, comme ceci :

```js
intersection([1, 2, 3], [4, 3, 2]); // [2, 3]
```

Cela renverra un tableau contenant les éléments qui existent dans les deux tableaux, les doublons étant éliminés.
