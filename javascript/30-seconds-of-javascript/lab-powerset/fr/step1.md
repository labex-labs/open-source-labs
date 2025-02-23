# Comment générer la puissance d'un ensemble en JavaScript

Pour générer la puissance d'un ensemble d'un tableau donné de nombres en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.reduce()` combinée avec la méthode `Array.prototype.map()` pour itérer sur les éléments et les combiner en un tableau contenant toutes les combinaisons.
3. Implémentez le code suivant :

```js
const powerset = (arr) =>
  arr.reduce((a, v) => a.concat(a.map((r) => r.concat(v))), [[]]);
```

4. Pour générer la puissance d'un ensemble, appelez la fonction `powerset()` et passez le tableau en tant qu'argument. Par exemple :

```js
powerset([1, 2]); // [[], [1], [2], [1, 2]]
```

Cela retournera un tableau contenant tous les sous-ensembles possibles du tableau donné.
