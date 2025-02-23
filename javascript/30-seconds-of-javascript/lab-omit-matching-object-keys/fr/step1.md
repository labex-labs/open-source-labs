# Suppression de clés d'objet en fonction d'une fonction de rappel

Pour supprimer les clés d'un objet en fonction d'une fonction de rappel, utilisez la fonction `omitBy`.

- `omitBy` crée un objet composé des propriétés qui renvoient `falsy` pour la fonction donnée.
- `Object.keys()` et `Array.prototype.filter()` sont utilisés pour supprimer les clés pour lesquelles `fn` renvoie une valeur `truthy`.
- `Array.prototype.reduce()` convertit les clés filtrées en un objet avec les paires clé-valeur correspondantes.
- La fonction de rappel prend deux arguments : `value` et `key`.
- L'exemple ci-dessous montre comment `omitBy` est utilisé pour supprimer les clés numériques d'un objet.

```js
const omitBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => !fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});

omitBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number"); // { b: '2' }
```
