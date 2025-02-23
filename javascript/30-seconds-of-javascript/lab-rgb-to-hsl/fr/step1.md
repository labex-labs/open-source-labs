# Conversion RGB en HSL

Pour convertir un tuple de couleur RGB au format HSL, suivez ces étapes :

1. Ouvrez le Terminal/SSH pour commencer à pratiquer la programmation.
2. Tapez `node` et appuyez sur Entrée.
3. Utilisez la [formule de conversion RGB en HSL](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/) pour convertir au format approprié.
4. Assurez-vous que tous les paramètres d'entrée se situent dans la plage de [0, 255].
5. Les valeurs résultantes devraient se situer dans la plage de H : [0, 360], S : [0, 100], L : [0, 100].

Voici un exemple de la fonction RGBToHSL en JavaScript :

```js
const RGBToHSL = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const l = Math.max(r, g, b);
  const s = l - Math.min(r, g, b);
  const h = s
    ? l === r
      ? (g - b) / s
      : l === g
        ? 2 + (b - r) / s
        : 4 + (r - g) / s
    : 0;
  return [
    60 * h < 0 ? 60 * h + 360 : 60 * h,
    100 * (s ? (l <= 0.5 ? s / (2 * l - s) : s / (2 - (2 * l - s))) : 0),
    (100 * (2 * l - s)) / 2
  ];
};
```

Voici un exemple de l'utilisation de la fonction RGBToHSL :

```js
RGBToHSL(45, 23, 11); // [21.17647, 60.71428, 10.98039]
```
