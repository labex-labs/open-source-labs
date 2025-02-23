# Suppression d'éléments d'un tableau à partir de la fin jusqu'à ce qu'une condition soit remplie

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici une fonction qui supprime des éléments de la fin d'un tableau jusqu'à ce que la fonction passée renvoie `false`. Elle renvoie ensuite les éléments supprimés.

Pour l'utiliser, créez une copie inversée du tableau à l'aide de l'opérateur de propagation (`...`) et de `Array.prototype.reverse()`. Ensuite, bouclez sur la copie inversée à l'aide d'une boucle `for...of` sur `Array.prototype.entries()` jusqu'à ce que la valeur renvoyée par la fonction soit fausse.

La fonction de rappel, `fn`, accepte un seul argument qui est la valeur de l'élément. Enfin, renvoyez les éléments supprimés à l'aide de `Array.prototype.slice()`.

```js
const takeRightWhile = (arr, fn) => {
  for (const [i, val] of [...arr].reverse().entries())
    if (!fn(val)) return i === 0 ? [] : arr.slice(-i);
  return arr;
};
```

Voici un exemple d'utilisation de la fonction :

```js
takeRightWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```
