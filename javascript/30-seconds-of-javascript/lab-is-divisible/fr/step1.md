# Vérifier si un nombre est divisible

Pour vérifier si un nombre est divisible par un autre nombre en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez l'opérateur modulo (`%`) pour vérifier si le reste de la division est égal à `0`. Si c'est le cas, alors le nombre est divisible.

Voici une fonction d'exemple qui vérifie si le premier argument numérique est divisible par le second :

```js
const isDivisible = (dividend, divisor) => dividend % divisor === 0;
```

Vous pouvez tester cette fonction avec `isDivisible(6, 3)`, qui devrait renvoyer `true` car 6 est divisible par 3.
