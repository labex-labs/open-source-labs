# Conversion HSB en RGB

Pour convertir un tuple de couleur HSB au format RGB, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez la [formule de conversion HSB en RGB](https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB) pour convertir au format approprié.
- Les paramètres d'entrée doivent être dans la plage de H : [0, 360], S : [0, 100], B : [0, 100].
- Toutes les valeurs de sortie doivent être dans la plage de [0, 255].

Voici le code que vous pouvez utiliser pour convertir HSB en RGB :

```js
const HSBToRGB = (h, s, b) => {
  s /= 100;
  b /= 100;
  const k = (n) => (n + h / 60) % 6;
  const f = (n) => b * (1 - s * Math.max(0, Math.min(k(n), 4 - k(n), 1)));
  return [255 * f(5), 255 * f(3), 255 * f(1)];
};
```

Par exemple, si vous voulez convertir le tuple de couleur HSB (18, 81, 99) au format RGB, vous pouvez utiliser le code suivant :

```js
HSBToRGB(18, 81, 99); // [252.45, 109.31084999999996, 47.965499999999984]
```
