# Recherche de sous-chaîne insensible à la casse

Pour vérifier si une chaîne contient une sous-chaîne indépendamment de la casse, suivez ces étapes :

- Utilisez le constructeur `RegExp` avec le drapeau `'i'` pour créer une expression régulière qui correspond à la chaîne de recherche donnée `searchString`, en ignorant la casse.
- Utilisez `RegExp.prototype.test()` pour vérifier si la chaîne contient la sous-chaîne.

Voici un extrait de code d'exemple :

```js
const includesCaseInsensitive = (str, searchString) =>
  new RegExp(searchString, "i").test(str);
```

Pour tester cette fonction, vous pouvez exécuter :

```js
includesCaseInsensitive("Blue Whale", "blue"); // true
```
