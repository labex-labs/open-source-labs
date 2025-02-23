# Calculating the Factorial of a Number

Pour calculer la factorielle d'un nombre, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursivité pour calculer la factorielle.
3. Si `n` est inférieur ou égal à `1`, renvoyez `1`.
4. Sinon, renvoyez le produit de `n` et de la factorielle de `n - 1`.
5. Si `n` est un nombre négatif, lancez une `TypeError`.

Voici le code pour calculer la factorielle :

```js
const factorial = (n) =>
  n < 0
    ? (() => {
        throw new TypeError("Negative numbers are not allowed!");
      })()
    : n <= 1
      ? 1
      : n * factorial(n - 1);
```

Vous pouvez tester le code en appelant la fonction `factorial` avec un nombre en argument :

```js
factorial(6); // 720
```
