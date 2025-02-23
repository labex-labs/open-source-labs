# Fonction pour convertir une chaîne en slug d'URL

Pour convertir une chaîne en un slug qui peut être utilisé dans une URL, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez les méthodes `String.prototype.toLowerCase()` et `String.prototype.trim()` pour normaliser la chaîne.
3. Utilisez la méthode `String.prototype.replace()` pour remplacer les espaces, les tirets et les underscores par `-`, et supprimer les caractères spéciaux.
4. Implémentez le code suivant :

```js
const slugify = (str) =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
```

5. Testez la fonction avec l'entrée `slugify('Hello World!');` et elle devrait renvoyer la sortie `'hello-world'`.
