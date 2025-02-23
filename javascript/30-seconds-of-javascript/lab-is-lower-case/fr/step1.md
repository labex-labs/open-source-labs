# Fonction JavaScript pour Vérifier si une Chaîne est en Minuscules

Pour vérifier si une chaîne de caractères donnée est en minuscules, vous pouvez utiliser la fonction JavaScript suivante. Tout d'abord, convertissez la chaîne en minuscules en utilisant `String.prototype.toLowerCase()` puis comparez-la à la chaîne d'origine en utilisant l'égalité stricte (`===`).

```js
const isLowerCase = (str) => str === str.toLowerCase();
```

Voici un exemple d'utilisation :

```js
isLowerCase("abc"); // true
isLowerCase("a3@$"); // true
isLowerCase("Ab4"); // false
```

Pour utiliser cette fonction, ouvrez le Terminal/SSH et tapez `node`.
