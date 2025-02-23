# Suppression d'éléments d'un tableau jusqu'à ce qu'une condition soit remplie

Pour supprimer des éléments d'un tableau jusqu'à ce qu'une condition soit remplie et obtenir les éléments supprimés, suivez les étapes suivantes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Parcourez le tableau à l'aide d'une boucle `for...of` sur `Array.prototype.entries()` jusqu'à ce que la fonction passée en argument renvoie une valeur vraie.
- Utilisez `Array.prototype.slice()` pour renvoyer les éléments supprimés.
- La fonction de rappel, `fn`, accepte un seul argument qui est la valeur de l'élément.

Voici un extrait de code d'exemple :

```js
const takeUntil = (arr, fn) => {
  for (const [i, val] of arr.entries()) if (fn(val)) return arr.slice(0, i);
  return arr;
};

takeUntil([1, 2, 3, 4], (n) => n >= 3); // [1, 2]
```

Dans l'exemple ci-dessus, la fonction `takeUntil()` est utilisée pour supprimer des éléments du tableau `[1, 2, 3, 4]` jusqu'à ce que la valeur soit supérieure ou égale à 3. La sortie est `[1, 2]`.
