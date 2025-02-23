# Comment obtenir un tableau sans le dernier élément

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Voici comment vous pouvez renvoyer tous les éléments d'un tableau sauf le dernier :

- Utilisez `Array.prototype.slice()` pour renvoyer tous les éléments du tableau sauf le dernier.

```js
const initial = (arr) => arr.slice(0, -1);
```

Voici un exemple :

```js
initial([1, 2, 3]); // [1, 2]
```
