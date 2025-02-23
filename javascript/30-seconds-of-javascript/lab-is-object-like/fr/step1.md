# Vérifier si une valeur est de type objet

Pour vérifier si une valeur est de type objet, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node` pour commencer à pratiquer la programmation.
3. Vérifiez si la valeur fournie n'est pas `null` et si son `typeof` est égal à `'object'`.

Voici le code que vous pouvez utiliser :

```js
const isObjectLike = (val) => val !== null && typeof val === "object";
```

Vous pouvez tester cette fonction avec les exemples suivants :

```js
isObjectLike({}); // true
isObjectLike([1, 2, 3]); // true
isObjectLike((x) => x); // false
isObjectLike(null); // false
```
