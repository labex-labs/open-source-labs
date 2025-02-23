# Vérifier si un élément quelconque d'un tableau est évalué comme vrai

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Pour vérifier si un élément quelconque dans une collection renvoie `true` sur la base d'une fonction fournie, utilisez `Array.prototype.some()`. Si vous voulez utiliser la fonction `Boolean` par défaut, vous pouvez omettre le second argument, `fn`.

Voici un exemple de code :

```js
const any = (arr, fn = Boolean) => arr.some(fn);
```

Vous pouvez le tester à l'aide des exemples suivants :

```js
any([0, 1, 2, 0], (x) => x >= 2); // true
any([0, 0, 1, 0]); // true
```
