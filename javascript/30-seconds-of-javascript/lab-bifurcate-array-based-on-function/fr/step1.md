# Fonction pour diviser un tableau en deux groupes

Pour diviser un tableau en deux groupes en fonction du résultat d'une fonction donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez les méthodes `Array.prototype.reduce()` et `Array.prototype.push()` pour ajouter des éléments aux groupes. Cela est basé sur la valeur renvoyée par la fonction donnée `fn` pour chaque élément.
3. Si `fn` renvoie une valeur véridique pour un élément quelconque, ajoutez-le au premier groupe. Sinon, ajoutez-le au second groupe.

Voici le code :

```js
const bifurcateBy = (arr, fn) =>
  arr.reduce(
    (acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc),
    [[], []]
  );
```

Par exemple, si vous appelez `bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b')`, la fonction renverra `[ ['beep', 'boop', 'bar'], ['foo'] ]`.
