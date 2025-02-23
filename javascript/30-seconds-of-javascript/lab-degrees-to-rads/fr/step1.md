# Conversion de degrés en radians

Pour convertir un angle de degrés en radians, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node` pour commencer à coder.
3. Utilisez la formule de conversion de degrés en radians avec `Math.PI`.
4. Appliquez la formule à l'angle en degrés pour obtenir l'angle en radians.

Voici la formule en JavaScript :

```js
const degreesToRads = (deg) => (deg * Math.PI) / 180.0;
```

Par exemple, si vous voulez convertir 90 degrés en radians, vous pouvez utiliser la fonction `degreesToRads` comme ceci :

```js
degreesToRads(90.0); // ~1.5708
```
