# Calcul de la distance vectorielle

Pour calculer la distance entre deux vecteurs, suivez ces étapes :

1. Ouvrez le Terminal/SSH pour commencer à pratiquer la programmation.
2. Tapez `node` pour commencer.
3. Utilisez `Array.prototype.reduce()`, `Math.pow()` et `Math.sqrt()` pour trouver la distance euclidienne entre les vecteurs.
4. Appliquez la formule `vectorDistance`, présentée ci-dessous :

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5. Testez la formule en entrant deux vecteurs au format suivant : `vectorDistance([10, 0, 5], [20, 0, 10]);`
6. La sortie sera la distance entre les deux vecteurs : `11.180339887498949`.
