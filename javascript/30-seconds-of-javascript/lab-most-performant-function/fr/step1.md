# Comment trouver la fonction la plus performante en JavaScript

Pour trouver la fonction la plus performante en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer le codage.
2. Utilisez `Array.prototype.map()` pour générer un tableau où chaque valeur est le temps total pris pour exécuter la fonction après `iterations` fois.
3. Utilisez la différence entre les valeurs de `performance.now()` avant et après pour obtenir le temps total en millisecondes avec un haut degré de précision.
4. Utilisez `Math.min()` pour trouver le temps d'exécution minimum et renvoyer l'index de ce temps le plus court qui correspond à l'index de la fonction la plus performante.
5. Si vous omettez le second argument, `iterations`, la fonction utilisera une valeur par défaut de `10000` itérations.
6. Gardez à l'esprit que plus vous utilisez d'itérations, plus le résultat sera fiable, mais plus cela prendra de temps.

Voici un extrait de code d'exemple :

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

Pour utiliser cette fonction, passez un tableau de fonctions en tant que premier argument et le nombre d'itérations en tant que second argument (optionnel). Par exemple :

```js
mostPerformant([
  () => {
    // Parcourt le tableau entier avant de renvoyer `false`
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // N'a besoin que d'atteindre l'index `1` avant de renvoyer `false`
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
