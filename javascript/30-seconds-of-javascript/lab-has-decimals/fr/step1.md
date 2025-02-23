# Comment vérifier si un nombre a des chiffres décimaux

Pour vérifier si un nombre a des chiffres décimaux, vous pouvez utiliser l'opérateur modulo en JavaScript. Suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez l'opérateur modulo (`%`) pour vérifier si le nombre est divisible par `1`.
3. Si le résultat n'est pas égal à zéro, alors le nombre a des chiffres décimaux.

Voici un exemple de code pour vérifier si un nombre a des chiffres décimaux :

```js
const hasDecimals = (num) => num % 1 !== 0;
```

Vous pouvez tester la fonction en l'appelant avec différents nombres, comme ceci :

```js
hasDecimals(1); // false
hasDecimals(1.001); // true
```
