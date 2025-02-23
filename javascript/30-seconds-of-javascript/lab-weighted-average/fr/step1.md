# Comment calculer la moyenne pondérée en JavaScript

Pour calculer la moyenne pondérée de deux ou plusieurs nombres en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()` pour créer la somme pondérée des valeurs et la somme des poids.
3. Divisez la somme pondérée des valeurs par la somme des poids pour obtenir la moyenne pondérée.

Voici le code JavaScript pour la fonction `weightedAverage` :

```js
const weightedAverage = (nums, weights) => {
  const [sum, weightSum] = weights.reduce(
    (acc, w, i) => {
      acc[0] = acc[0] + nums[i] * w;
      acc[1] = acc[1] + w;
      return acc;
    },
    [0, 0]
  );
  return sum / weightSum;
};
```

Vous pouvez utiliser la fonction `weightedAverage` pour calculer la moyenne pondérée d'un tableau de nombres et d'un tableau de poids comme ceci :

```js
weightedAverage([1, 2, 3], [0.6, 0.2, 0.3]); // 1.72727
```
