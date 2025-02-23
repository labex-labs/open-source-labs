# Comment modifier la luminosité d'une couleur HSL

Pour modifier la valeur de luminosité d'une chaîne de caractères de couleur `hsl()`, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez `String.prototype.match()` pour obtenir un tableau de trois chaînes de caractères avec les valeurs numériques de la chaîne `hsl()`.

3. Utilisez `Array.prototype.map()` en combinaison avec `Number` pour convertir les chaînes de caractères en un tableau de valeurs numériques.

4. Assurez-vous que la valeur de luminosité est dans la plage valide (entre `0` et `100`) en utilisant `Math.max()` et `Math.min()`.

5. Utilisez une littérale de gabarit pour créer une nouvelle chaîne de caractères `hsl()` avec la valeur de luminosité mise à jour.

Voici un extrait de code d'exemple qui met en œuvre ces étapes :

```js
const changeLightness = (delta, hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);

  const newLightness = Math.max(
    0,
    Math.min(100, lightness + parseFloat(delta))
  );

  return `hsl(${hue}, ${saturation}%, ${newLightness}%)`;
};
```

Vous pouvez ensuite appeler la fonction `changeLightness()` avec une valeur de delta et une chaîne de caractères `hsl()` pour obtenir une nouvelle chaîne de caractères `hsl()` avec la valeur de luminosité mise à jour. Par exemple :

```js
changeLightness(10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 60%)'
changeLightness(-10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 40%)'
```
