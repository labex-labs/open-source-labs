# Calcul de la distance de Hamming

Pour calculer la distance de Hamming entre deux valeurs, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer le codage.
2. Utilisez l'opérateur XOR (`^`) pour trouver la différence binaire entre les deux nombres.
3. Convertissez le résultat en une chaîne binaire en utilisant `Number.prototype.toString()`.
4. Comptez le nombre de `1` dans la chaîne en utilisant `String.prototype.match()`.
5. Retournez le compte.

Voici le code pour la fonction `hammingDistance` :

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || "").length;
```

Vous pouvez tester la fonction en exécutant `hammingDistance(2, 3); // 1`.
