# Convertir HSL en tableau

Pour convertir une chaîne de caractères de couleur `hsl()` en un tableau de valeurs, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `String.prototype.match()` pour obtenir un tableau de 3 chaînes de caractères avec les valeurs numériques.
3. Utilisez `Array.prototype.map()` en combinaison avec `Number` pour les convertir en un tableau de valeurs numériques.

Voici le code pour convertir une chaîne de caractères de couleur `hsl()` en un tableau de valeurs numériques :

```js
const toHSLArray = (hslStr) => hslStr.match(/\d+/g).map(Number);
```

Utilisation exemple :

```js
toHSLArray("hsl(50, 10%, 10%)"); // [50, 10, 10]
```
