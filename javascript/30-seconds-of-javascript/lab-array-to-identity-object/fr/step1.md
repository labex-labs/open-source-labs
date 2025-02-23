# Voici comment convertir un tableau en un objet identité

Si vous voulez pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Pour convertir un tableau de valeurs en un objet avec les mêmes valeurs comme clés et valeurs, suivez ces étapes :

1. Utilisez `Array.prototype.map()` pour mapper chaque valeur à un tableau de paires clé-valeur.
2. Utilisez `Object.fromEntries()` pour convertir le tableau de paires clé-valeur en un objet.

Voici le code :

```js
const toIdentityObject = (arr) => Object.fromEntries(arr.map((v) => [v, v]));
```

Et voici un exemple :

```js
toIdentityObject(["a", "b"]); // { a: 'a', b: 'b' }
```
