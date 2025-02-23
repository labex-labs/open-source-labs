# Fonction pour compresser les espaces blancs dans une chaîne de caractères

Pour compresser les espaces blancs dans une chaîne de caractères, utilisez la fonction `compactWhitespace()`.

- Elle utilise `String.prototype.replace()` avec une expression régulière pour remplacer toutes les occurrences de 2 caractères d'espace blanc ou plus par un seul espace.
- La fonction prend une chaîne de caractères en argument et renvoie la chaîne de caractères compressée.

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

Utilisation de l'exemple :

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
