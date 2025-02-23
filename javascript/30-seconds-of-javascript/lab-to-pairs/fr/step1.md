# Conversion d'un objet en paires

Pour convertir un objet en un tableau de paires clé-valeur, utilisez la fonction `toPairs`. Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

La fonction `toPairs` fonctionne de la manière suivante :

- Tout d'abord, elle vérifie si `Symbol.iterator` est défini pour l'objet itérable donné.
- Si `Symbol.iterator` est défini, elle utilise `Array.prototype.entries()` pour obtenir un itérateur pour l'objet puis convertit le résultat en un tableau d'éléments clé-valeur à l'aide de `Array.from()`.
- Si `Symbol.iterator` n'est pas défini pour l'objet, elle utilise `Object.entries()` à la place.

Voici le code pour la fonction `toPairs` :

```js
const toPairs = (obj) =>
  obj[Symbol.iterator] instanceof Function && obj.entries instanceof Function
    ? Array.from(obj.entries())
    : Object.entries(obj);
```

Vous pouvez utiliser la fonction `toPairs` avec différents types d'objets, tels que :

```js
toPairs({ a: 1, b: 2 }); // [['a', 1], ['b', 2]]
toPairs([2, 4, 8]); // [[0, 2], [1, 4], [2, 8]]
toPairs("shy"); // [['0','s'], ['1', 'h'], ['2', 'y']]
toPairs(new Set(["a", "b", "c", "a"])); // [['a', 'a'], ['b', 'b'], ['c', 'c']]
```
