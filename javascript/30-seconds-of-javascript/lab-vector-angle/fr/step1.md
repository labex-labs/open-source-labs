# Calcul de l'angle de vecteur

Pour calculer l'angle (theta) entre deux vecteurs, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()`, `Math.pow()` et `Math.sqrt()` pour calculer la norme de chaque vecteur et le produit scalaire des deux vecteurs.
3. Utilisez `Math.acos()` pour calculer l'arccosinus et obtenir la valeur de theta.

Voici un extrait de code d'exemple :

```js
const vectorAngle = (x, y) => {
  let mX = Math.sqrt(x.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  let mY = Math.sqrt(y.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  return Math.acos(x.reduce((acc, n, i) => acc + n * y[i], 0) / (mX * mY));
};

vectorAngle([3, 4], [4, 3]); // 0.283794109208328
```

Cette fonction prend deux tableaux (`x` et `y`) en arguments et renvoie l'angle (en radians) entre eux.
