# Suppression d'éléments d'un tableau en fonction d'une condition

Pour supprimer des éléments d'un tableau en fonction d'une condition, ouvrez le Terminal/SSH et tapez `node`.

La fonction `takeWhile` supprime des éléments d'un tableau jusqu'à ce que la fonction passée renvoie `false`, puis renvoie les éléments supprimés.

Voici les étapes pour utiliser la fonction `takeWhile` :

- Parcourez le tableau à l'aide d'une boucle `for...of` sur `Array.prototype.entries()`.
- Bouclez jusqu'à ce que la valeur renvoyée par la fonction soit fausse.
- Retournez les éléments supprimés à l'aide de `Array.prototype.slice()`.
- La fonction de rappel `fn` accepte un seul argument qui est la valeur de l'élément.

Utilisez le code suivant pour implémenter la fonction `takeWhile` :

```js
const takeWhile = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (!fn(val)) return arr.slice(0, i);
  return arr;
};
```

Voici un exemple d'utilisation de la fonction `takeWhile` pour supprimer des éléments d'un tableau en fonction d'une condition :

```js
takeWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
