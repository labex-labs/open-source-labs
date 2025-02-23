# Utiliser l'ET logique avec des fonctions

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Pour vérifier si deux fonctions renvoient `true` pour un ensemble donné d'arguments, utilisez l'opérateur logique ET (`&&`).

```js
const both =
  (f, g) =>
  (...args) =>
    f(...args) && g(...args);
```

Le code ci-dessus crée une nouvelle fonction `both` qui prend deux fonctions `f` et `g` en entrée et renvoie une autre fonction qui appelle `f` et `g` avec les arguments fournis et renvoie `true` seulement si les deux fonctions renvoient `true`.

Par exemple, pour vérifier si un nombre est à la fois positif et pair, on peut utiliser les fonctions `isEven` et `isPositive` avec `both` comme suit :

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveEven = both(isEven, isPositive);
isPositiveEven(4); // true
isPositiveEven(-2); // false
```

Ici, `isPositiveEven` est une nouvelle fonction qui vérifie si un nombre donné est à la fois positif et pair en utilisant la fonction `both` avec `isEven` et `isPositive` en entrée.
