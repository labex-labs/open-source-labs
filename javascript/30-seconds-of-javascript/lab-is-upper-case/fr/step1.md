# Fonction pour vérifier si une chaîne est en majuscules

Pour vérifier si une chaîne est en majuscules, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node`.
3. Utilisez la fonction `isUpperCase()` pour convertir la chaîne donnée en majuscules, à l'aide de `String.prototype.toUpperCase()`, et la comparer à la chaîne d'origine.
4. La fonction renverra `true` si la chaîne est en majuscules et `false` si elle ne l'est pas.

Voici un exemple de code :

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
