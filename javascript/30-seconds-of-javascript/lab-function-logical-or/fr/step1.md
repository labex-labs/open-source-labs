# Utilisation de l'opérateur logique ou pour les fonctions

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

L'opérateur logique ou (`||`) peut être utilisé pour vérifier si au moins une fonction renvoie `true` pour un ensemble donné d'arguments. Pour ce faire, appelez les deux fonctions avec les `args` fournis et appliquez l'opérateur logique ou sur leurs résultats.

Voici une implémentation exemple de la fonction `either` :

```js
const either =
  (f, g) =>
  (...args) =>
    f(...args) || g(...args);
```

Et voici un exemple d'utilisation de la fonction `either` avec deux fonctions `isEven` et `isPositive` :

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveOrEven = either(isPositive, isEven);
isPositiveOrEven(4); // true
isPositiveOrEven(3); // true
```

Dans cet exemple, `isPositiveOrEven` renvoie `true` pour à la fois `4` et `3` car `isEven` renvoie `true` pour `4` et `isPositive` renvoie `true` pour `3`.
