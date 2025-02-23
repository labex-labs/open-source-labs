# Vérification d'une valeur `undefined`

Pour vérifier si une valeur est `undefined`, ouvrez le Terminal/SSH et tapez `node`.

- Utilisez l'opérateur d'égalité stricte pour vérifier si `val` est égal à `undefined`.

```js
const isUndefined = (val) => val === undefined;
```

```js
isUndefined(undefined); // true
```

Ce code vérifiera si la valeur spécifiée est `undefined`.
