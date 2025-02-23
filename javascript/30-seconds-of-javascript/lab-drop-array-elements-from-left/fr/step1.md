# Suppression d'éléments d'un tableau du côté gauche

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici une fonction qui crée un nouveau tableau avec un nombre spécifié d'éléments supprimés du côté gauche :

```js
const drop = (arr, n = 1) => arr.slice(n);
```

La fonction utilise `Array.prototype.slice()` pour supprimer le nombre spécifié d'éléments du côté gauche. Si vous omettez le dernier argument, `n`, la fonction utilisera une valeur par défaut de `1`.

Voici quelques exemples d'utilisation de la fonction `drop` :

```js
drop([1, 2, 3]); // [2, 3]
drop([1, 2, 3], 2); // [3]
drop([1, 2, 3], 42); // []
```
