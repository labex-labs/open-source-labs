# Fonction pour convertir une chaîne en cas titre

Pour convertir une chaîne donnée en cas titre, utilisez la fonction suivante. Elle utilise `String.prototype.match()` pour diviser la chaîne en mots à l'aide d'une expression régulière appropriée. Ensuite, elle les combine à l'aide de `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` et `String.prototype.toUpperCase()`. Cela met en majuscule la première lettre de chaque mot et ajoute un espace entre eux.

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

Voici quelques exemples d'utilisation de la fonction :

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
