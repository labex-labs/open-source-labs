# Supprimer des éléments d'un tableau à partir de la droite

Pour supprimer un nombre spécifié d'éléments à partir de la droite d'un tableau, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.slice()` pour supprimer le nombre spécifié d'éléments à partir de la droite.
3. Si vous voulez supprimer seulement un élément, vous pouvez omettre le dernier argument, `n`, et la valeur par défaut de `1` sera utilisée.

Voici un extrait de code d'exemple :

```js
const dropRight = (arr, n = 1) => arr.slice(0, -n);
```

Vous pouvez tester cette fonction avec les exemples suivants :

```js
dropRight([1, 2, 3]); // [1, 2]
dropRight([1, 2, 3], 2); // [1]
dropRight([1, 2, 3], 42); // []
```
