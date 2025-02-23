# Fonction pour diviser un tableau en deux groupes

Pour utiliser cette fonction pour diviser un tableau en deux groupes en fonction des valeurs, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction `bifurcate()`, qui divise les valeurs en deux groupes en fonction du résultat du tableau `filter` donné.
3. Pour implémenter la fonction, utilisez `Array.prototype.reduce()` et `Array.prototype.push()` pour ajouter des éléments aux groupes, en fonction du tableau `filter`.
4. Si `filter` a une valeur véridique pour un élément quelconque, ajoutez-le au premier groupe ; sinon, ajoutez-le au second groupe.

Voici le code de la fonction `bifurcate()` :

```js
const bifurcate = (arr, filter) =>
  arr.reduce(
    (acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc),
    [[], []]
  );
```

Vous pouvez appeler la fonction `bifurcate()` avec un tableau de valeurs et un tableau de filtre correspondant pour diviser les valeurs en deux groupes. Par exemple :

```js
bifurcate(["beep", "boop", "foo", "bar"], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]
```
