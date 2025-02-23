# Calculer la distance entre deux points

Pour calculer la distance entre deux points, suivez les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Math.hypot()` pour calculer la distance euclidienne entre deux points.
3. Implémentez le code ci-dessous, en remplaçant les valeurs de `x0`, `y0`, `x1` et `y1` par les coordonnées de vos points.

```js
const distance = (x0, y0, x1, y1) => Math.hypot(x1 - x0, y1 - y0);
```

Voici un exemple d'utilisation de cette fonction :

```js
distance(1, 1, 2, 3); // ~2.2361
```

Cela affichera la distance entre les points `(1, 1)` et `(2, 3)`.
