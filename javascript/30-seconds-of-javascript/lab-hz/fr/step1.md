# Calcul de la fréquence d'une fonction

Pour mesurer la fréquence d'exécution d'une fonction par seconde (hz/hertz), utilisez la fonction `hz`. Vous pouvez le faire en suivant ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `performance.now()` pour obtenir la différence en millisecondes avant et après la boucle d'itération pour calculer le temps écoulé lors de l'exécution de la fonction `iterations` fois.
3. Convertissez les millisecondes en secondes et divisez-la par le temps écoulé pour retourner le nombre de cycles par seconde.
4. Si vous voulez utiliser la valeur par défaut de 100 itérations, omettez le second argument, `iterations`.

```js
const hz = (fn, iterations = 100) => {
  const before = performance.now();
  for (let i = 0; i < iterations; i++) fn();
  return (1000 * iterations) / (performance.now() - before);
};
```

Voici un exemple d'utilisation de la fonction `hz` pour comparer les performances de deux fonctions qui calculent la somme d'un tableau de 10 000 nombres :

```js
const numbers = Array(10000)
  .fill()
  .map((_, i) => i);

const sumReduce = () => numbers.reduce((acc, n) => acc + n, 0);
const sumForLoop = () => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) sum += numbers[i];
  return sum;
};

Math.round(hz(sumReduce)); // 572
Math.round(hz(sumForLoop)); // 4784
```

Dans cet exemple, `sumReduce` est plus rapide que `sumForLoop` car elle a une fréquence d'exécution de fonction plus faible.
