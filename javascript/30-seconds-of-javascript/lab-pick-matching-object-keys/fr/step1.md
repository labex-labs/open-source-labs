# Fonction pour sélectionner les clés d'un objet qui correspondent à une condition donnée

Pour sélectionner les clés d'un objet qui correspondent à une condition donnée, utilisez la fonction `pickBy()`. Cette fonction crée un nouvel objet composé des propriétés pour lesquelles la fonction donnée renvoie une valeur véridique.

- Utilisez `Object.keys()` et `Array.prototype.filter()` pour supprimer les clés pour lesquelles `fn` renvoie une valeur fausse.
- Utilisez `Array.prototype.reduce()` pour convertir les clés filtrées en un objet avec les paires clé-valeur correspondantes.
- La fonction de rappel est appelée avec deux arguments : (valeur, clé).

Voici le code pour la fonction `pickBy()` :

```js
const pickBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});
```

Vous pouvez utiliser cette fonction pour sélectionner les clés qui correspondent à une condition. Par exemple :

```js
pickBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number");
// { 'a': 1, 'c': 3 }
```
