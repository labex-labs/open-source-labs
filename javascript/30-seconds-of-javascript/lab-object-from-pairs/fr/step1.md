# Création d'un objet à partir de paires clé-valeur

Pour créer un objet à partir de paires clé-valeur, utilisez la fonction `objectFromPairs`.

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- La fonction utilise `Array.prototype.reduce()` pour créer et combiner les paires clé-valeur.
- Pour une implémentation plus simple, vous pouvez également utiliser [`Object.fromEntries()`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries).

```js
const objectFromPairs = (arr) =>
  arr.reduce((a, [key, val]) => ((a[key] = val), a), {});
```

Utilisation de l'exemple :

```js
objectFromPairs([
  ["a", 1],
  ["b", 2]
]); // {a: 1, b: 2}
```
