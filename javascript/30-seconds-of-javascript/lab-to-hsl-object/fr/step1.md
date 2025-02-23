# Conversion de HSL en Objet

Pour convertir une chaîne de caractères de couleur `hsl()` en un objet avec les valeurs numériques de chaque couleur, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez `String.prototype.match()` pour obtenir un tableau de 3 chaînes de caractères avec les valeurs numériques.
- Convertissez les chaînes de caractères en un tableau de valeurs numériques en utilisant `Array.prototype.map()` en combinaison avec `Number`.
- Stockez les valeurs dans des variables nommées en utilisant la désagrégation de tableau.
- Créez un objet approprié à partir des variables nommées.

```js
const toHSLObject = (hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);
  return { hue, saturation, lightness };
};
```

Utilisation de l'exemple :

```js
toHSLObject("hsl(50, 10%, 10%)"); // { hue: 50, saturation: 10, lightness: 10 }
```
