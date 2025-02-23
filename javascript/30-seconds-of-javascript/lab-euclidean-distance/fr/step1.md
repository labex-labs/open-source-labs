# Calcul de la distance euclidienne

Pour calculer la distance entre deux points dans un nombre quelconque de dimensions, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.keys()` et `Array.prototype.map()` pour mapper chaque coordonnée à sa différence entre les deux points.
3. Utilisez `Math.hypot()` pour calculer la distance euclidienne entre les deux points.

Voici un extrait de code d'exemple pour vous aider à commencer :

```js
const euclideanDistance = (a, b) =>
  Math.hypot(...Object.keys(a).map((k) => b[k] - a[k]));
```

Vous pouvez tester la fonction avec ces entrées d'échantillonnage :

```js
euclideanDistance([1, 1], [2, 3]); // ~2.2361
euclideanDistance([1, 1, 1], [2, 3, 2]); // ~2.4495
```
