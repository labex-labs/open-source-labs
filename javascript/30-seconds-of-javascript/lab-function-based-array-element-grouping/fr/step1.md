# Comment regrouper les éléments d'un tableau

Si vous voulez pratiquer la programmation, vous pouvez commencer par ouvrir le Terminal/SSH et taper `node`. Une fois que vous êtes prêt, vous pouvez regrouper les éléments d'un tableau en fonction d'une fonction donnée en utilisant les étapes suivantes :

1. Utilisez `Array.prototype.map()` pour mapper les valeurs du tableau à un nom de fonction ou de propriété.
2. Utilisez `Array.prototype.reduce()` pour créer un objet dont les clés sont produites à partir des résultats de la mise en correspondance.

Voici un extrait de code d'exemple :

```js
const groupBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val, i) => {
      acc[val] = (acc[val] || []).concat(arr[i]);
      return acc;
    }, {});
```

Pour tester le code, vous pouvez utiliser les exemples suivants :

```js
groupBy([6.1, 4.2, 6.3], Math.floor); // {4: [4.2], 6: [6.1, 6.3]}
groupBy(["one", "two", "three"], "length"); // {3: ['one', 'two'], 5: ['three']}
```

Cela retournera des objets avec des clés basées sur la fonction spécifiée et des valeurs qui sont des tableaux des éléments originaux qui correspondent à la fonction.
