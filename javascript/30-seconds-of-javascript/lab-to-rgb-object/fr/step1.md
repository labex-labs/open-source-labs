# Conversion de RGB en Objet

Pour convertir une chaîne de caractères de couleur `rgb()` en un objet avec les valeurs de chaque couleur, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `String.prototype.match()` pour obtenir un tableau de 3 chaînes de caractères avec les valeurs numériques.
3. Utilisez `Array.prototype.map()` en combinaison avec `Number` pour les convertir en un tableau de valeurs numériques.
4. Utilisez la décomposition d'objets pour stocker les valeurs dans des variables nommées et créer un objet approprié à partir d'elles.

Voici le code que vous pouvez utiliser :

```js
const toRGBObject = (rgbStr) => {
  const [red, green, blue] = rgbStr.match(/\d+/g).map(Number);
  return { red, green, blue };
};

toRGBObject("rgb(255, 12, 0)"); // {red: 255, green: 12, blue: 0}
```
