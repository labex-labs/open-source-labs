# Fonction de vérification de la vérité pour une collection

Pour pratiquer le codage, tapez `node` dans le Terminal/SSH.

Voici une fonction qui vérifie si une fonction prédicat est vraie pour tous les éléments d'une collection.

- Utilisez `Array.prototype.every()` pour vérifier si chaque objet passé possède la propriété spécifiée et si elle renvoie une valeur vraie.

```js
const truthCheckCollection = (collection, pre) =>
  collection.every((obj) => obj[pre]);
```

Utilisation exemple :

```js
truthCheckCollection(
  [
    { user: "Tinky-Winky", sex: "male" },
    { user: "Dipsy", sex: "male" }
  ],
  "sex"
); // true
```
