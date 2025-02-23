# Calculating Percentile of Matches

Pour calculer le centile de correspondances dans le tableau donné ci-dessous ou égales à une valeur donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer la pratique de codage.
2. Utilisez la méthode `Array.prototype.reduce()` pour calculer le nombre de valeurs inférieures à la valeur donnée et le nombre de valeurs égales à la valeur donnée.
3. Appliquez la formule du centile pour obtenir le pourcentage de correspondances.
4. Voici un extrait de code d'exemple :

```js
const percentile = (arr, val) =>
  (100 *
    arr.reduce(
      (acc, v) => acc + (v < val ? 1 : 0) + (v === val ? 0.5 : 0),
      0
    )) /
  arr.length;
```

5. Pour tester la fonction, utilisez cet extrait de code d'exemple :

```js
percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6); // Sortie : 55
```

Cette fonction renverra le pourcentage de correspondances dans le tableau donné qui sont inférieures ou égales à la valeur donnée.
