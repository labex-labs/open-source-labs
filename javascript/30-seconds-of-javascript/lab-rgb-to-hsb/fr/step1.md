# Conversion RGB en HSB

Pour convertir un tuple de couleurs RGB au format HSB, vous pouvez suivre ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la [formule de conversion RGB en HSB](https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB) pour convertir le tuple de couleurs RGB au format HSB approprié.
3. La plage de paramètres d'entrée est [0, 255], tandis que les valeurs résultantes ont une plage de :

- H : [0, 360]
- S : [0, 100]
- B : [0, 100]

Voici la fonction en JavaScript :

```js
const RGBToHSB = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const v = Math.max(r, g, b),
    n = v - Math.min(r, g, b);
  const h =
    n === 0
      ? 0
      : n && v === r
        ? (g - b) / n
        : v === g
          ? 2 + (b - r) / n
          : 4 + (r - g) / n;
  return [60 * (h < 0 ? h + 6 : h), v && (n / v) * 100, v * 100];
};
```

Vous pouvez appeler la fonction comme ceci :

```js
RGBToHSB(252, 111, 48);
// [18.529411764705856, 80.95238095238095, 98.82352941176471]
```
