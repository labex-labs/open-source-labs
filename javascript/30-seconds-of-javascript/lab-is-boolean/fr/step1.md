# Vérifier si une valeur est booléenne

Pour vérifier si une valeur est un primitif booléen en JavaScript, utilisez l'opérateur `typeof` avec l'opérateur de comparaison `===`.

```js
const isBoolean = (val) => typeof val === "boolean";
```

Voici un exemple de la manière d'utiliser la fonction `isBoolean()` pour vérifier si une valeur est booléenne :

```js
isBoolean(null); // renvoie false
isBoolean(false); // renvoie true
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
