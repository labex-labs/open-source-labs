# Une fonction pour trouver la différence symétrique entre deux tableaux

Pour trouver la différence symétrique entre deux tableaux en utilisant une fonction donnée comme comparateur, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez les méthodes `Array.prototype.filter()` et `Array.prototype.findIndex()` pour trouver les valeurs appropriées.
3. Utilisez le code donné pour effectuer l'opération.

```js
const symmetricDifferenceWith = (arr, val, comp) => [
  ...arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1),
  ...val.filter((a) => arr.findIndex((b) => comp(a, b)) === -1)
];
```

Par exemple, considérez l'entrée suivante :

```js
symmetricDifferenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
); // [1, 1.2, 3.9]
```

Le code ci-dessus renverra `[1, 1.2, 3.9]` comme différence symétrique entre les deux tableaux.
