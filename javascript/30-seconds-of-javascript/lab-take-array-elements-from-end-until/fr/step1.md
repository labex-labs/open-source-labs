# Suppression d'éléments d'un tableau à partir de la fin jusqu'à ce qu'une condition soit satisfaite

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction supprime des éléments de la fin d'un tableau jusqu'à ce que la fonction passée renvoie `true`, puis elle renvoie les éléments supprimés.

Voici comment elle fonctionne :

- Tout d'abord, créez une copie inversée du tableau en utilisant l'opérateur de propagation (`...`) et `Array.prototype.reverse()`.
- Ensuite, parcourez la copie inversée en utilisant une boucle `for...of` sur `Array.prototype.entries()` jusqu'à ce que la valeur renvoyée par la fonction soit évaluée comme vraie.
- Après cela, renvoyez les éléments supprimés en utilisant `Array.prototype.slice()`.
- La fonction de rappel, `fn`, accepte un seul argument qui est la valeur de l'élément.

Voici le code :

```js
const takeRightUntil = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Voici un exemple d'utilisation de cette fonction :

```js
takeRightUntil([1, 2, 3, 4], (n) => n < 3); // [3, 4]
```
