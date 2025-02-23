# Comment vérifier si une valeur est nulle ou indéfinie en JavaScript

Pour déterminer si une valeur est `null` ou `undefined` en JavaScript, vous pouvez utiliser l'opérateur d'égalité stricte (`===`). Voici un extrait de code d'exemple qui vérifie si la valeur spécifiée est `null` ou `undefined` :

```js
const isNil = (val) => val === undefined || val === null;
```

Vous pouvez utiliser cette fonction pour vérifier si une valeur est `null` ou `undefined`, comme ceci :

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

Pour commencer à pratiquer la programmation en JavaScript, vous pouvez ouvrir le Terminal/SSH et taper `node`.
