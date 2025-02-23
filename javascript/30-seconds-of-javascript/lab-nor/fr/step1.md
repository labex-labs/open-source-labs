# Comment utiliser le Nor logique en JavaScript

Pour commencer à coder en JavaScript, accédez au Terminal/SSH et tapez `node`. Le Nor logique vérifie si aucun des arguments donnés n'est vrai. Pour renvoyer l'inverse de l'OU logique de deux valeurs, utilisez l'opérateur non logique (`!`). Voici un exemple :

```js
const nor = (a, b) => !(a || b);
```

Et voici quelques résultats :

```js
nor(true, true); // false
nor(true, false); // false
nor(false, false); // true
```
