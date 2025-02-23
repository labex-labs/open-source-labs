# Comment regrouper et compter les éléments d'un tableau avec JavaScript

Pour regrouper et compter les éléments d'un tableau avec JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.map()` pour mapper les valeurs d'un tableau à un nom de fonction ou de propriété.
3. Utilisez la méthode `Array.prototype.reduce()` pour créer un objet dont les clés sont produites à partir des résultats de la mise en correspondance.
4. Créez une fonction appelée `countBy` qui prend un tableau et une fonction en arguments.
5. À l'intérieur de la fonction `countBy`, utilisez un opérateur ternaire pour vérifier si l'argument passé est une fonction ou un nom de propriété. Si c'est une fonction, utilisez-la comme fonction de mise en correspondance. Si c'est un nom de propriété, accédez à cette propriété des éléments du tableau.
6. Utilisez la méthode `reduce()` pour créer un objet où chaque clé représente un élément unique du tableau et sa valeur est le nombre de fois qu'il apparaît dans le tableau.

Voici le code :

```js
const countBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});
```

Vous pouvez tester la fonction `countBy` avec les exemples suivants :

```js
countBy([6.1, 4.2, 6.3], Math.floor); // {4: 1, 6: 2}
countBy(["one", "two", "three"], "length"); // {3: 2, 5: 1}
countBy([{ count: 5 }, { count: 10 }, { count: 5 }], (x) => x.count); // {5: 2, 10: 1}
```
