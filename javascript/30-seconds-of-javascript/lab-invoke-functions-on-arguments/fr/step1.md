# Appel de fonctions sur des arguments

Pour exécuter du code à l'aide de Node.js, ouvrez le Terminal/SSH et tapez `node`.

Pour créer une fonction qui appelle chaque fonction fournie avec les arguments qu'elle reçoit et renvoie les résultats :

- Utilisez `Array.prototype.map()` et `Function.prototype.apply()` pour appliquer chaque fonction aux arguments donnés.

```js
const over =
  (...fns) =>
  (...args) =>
    fns.map((fn) => fn.apply(null, args));
```

Exemple :

```js
const minMax = over(Math.min, Math.max);
minMax(1, 2, 3, 4, 5); // [1, 5]
```
