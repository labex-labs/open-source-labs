# Vérifier si une valeur est une chaîne de caractères

Pour vérifier si une valeur est une chaîne de caractères, utilisez le mot-clé `typeof` suivi de la valeur que vous voulez vérifier. Cette méthode ne fonctionne que pour les primitives chaîne de caractères.

Voici un exemple de code qui vérifie si une valeur donnée est une chaîne de caractères :

```js
const isString = (val) => typeof val === "string";
```

Vous pouvez utiliser la fonction `isString` comme ceci :

```js
isString("10"); // true
```
