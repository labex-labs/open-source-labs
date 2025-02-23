# Convertir HSL en RGB à l'aide de JavaScript

Pour convertir un tuple de couleur au format HSL en RGB, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la [formule de conversion de HSL en RGB](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB) pour convertir le tuple de couleur au format approprié.
3. Assurez-vous que les paramètres d'entrée sont dans les plages suivantes : H : [0, 360], S : [0, 100], L : [0, 100].
4. Les valeurs de sortie devraient être dans la plage [0, 255].

Voici le code JavaScript pour la formule de conversion de HSL en RGB :

```js
const HSLToRGB = (h, s, l) => {
  s /= 100;
  l /= 100;
  const k = (n) => (n + h / 30) % 12;
  const a = s * Math.min(l, 1 - l);
  const f = (n) =>
    l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
  return [255 * f(0), 255 * f(8), 255 * f(4)];
};
```

Pour utiliser la fonction, fournissez les valeurs de H, S et L en tant qu'arguments :

```js
HSLToRGB(13, 100, 11); // [56.1, 12.155, 0]
```
