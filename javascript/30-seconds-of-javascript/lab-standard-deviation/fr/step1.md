# Écart-type

Pour calculer l'écart-type d'un tableau de nombres en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction `standardDeviation(arr, usePopulation = false)` fournie ci-dessous.
3. Passez un tableau de nombres en tant que premier argument à la fonction.
4. Omettez le second argument, `usePopulation`, pour obtenir l'écart-type d'échantillon. Définissez-le sur `true` pour obtenir l'écart-type de population.

```js
const standardDeviation = (arr, usePopulation = false) => {
  const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length;
  return Math.sqrt(
    arr
      .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
      .reduce((acc, val) => acc + val, 0) /
      (arr.length - (usePopulation ? 0 : 1))
  );
};
```

Utilisation de l'exemple :

```js
standardDeviation([10, 2, 38, 23, 38, 23, 21]); // 13.284434142114991 (échantillon)
standardDeviation([10, 2, 38, 23, 38, 23, 21], true); // 12.29899614287479 (population)
```
