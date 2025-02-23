# Convertisseur RGB en Hexadécimal

Pour convertir des valeurs RGB en un code de couleur hexadécimal :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction suivante :

```js
const RGBToHex = (r, g, b) =>
  ((r << 16) + (g << 8) + b).toString(16).padStart(6, "0");
```

3. Appelez la fonction en utilisant les valeurs RGB comme arguments pour obtenir une valeur hexadécimale à 6 chiffres.

Par exemple :

```js
RGBToHex(255, 165, 1); // 'ffa501'
```
