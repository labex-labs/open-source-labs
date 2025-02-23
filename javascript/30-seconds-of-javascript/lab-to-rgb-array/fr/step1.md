# Conversion d'une chaîne RGB en un tableau

Pour convertir une chaîne de caractères de couleur `rgb()` en un tableau de valeurs, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `String.prototype.match()` pour obtenir un tableau de 3 chaînes avec les valeurs numériques.
3. Utilisez `Array.prototype.map()` en combinaison avec `Number` pour les convertir en un tableau de valeurs numériques.

Voici le code que vous pouvez utiliser :

```js
const toRGBArray = (rgbStr) => rgbStr.match(/\d+/g).map(Number);
```

Pour tester la fonction, appelez-la avec une chaîne de caractères de couleur `rgb()` en tant qu'argument, comme ceci :

```js
toRGBArray("rgb(255, 12, 0)"); // [255, 12, 0]
```
