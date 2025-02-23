# Comment remplacer ou ajouter une valeur dans un tableau

Pour remplacer un élément dans un tableau ou l'ajouter s'il n'existe pas, suivez ces étapes :

1. Utilisez l'opérateur de propagation (`...`) pour créer une copie superficielle du tableau.
2. Utilisez `Array.prototype.findIndex()` pour trouver l'index du premier élément qui satisfait la fonction de comparaison fournie `compFn`.
3. Si aucun tel élément n'est trouvé, utilisez `Array.prototype.push()` pour ajouter la nouvelle valeur au tableau.
4. Sinon, utilisez `Array.prototype.splice()` pour remplacer la valeur à l'index trouvé par la nouvelle valeur.

Voici un exemple de mise en œuvre de cette fonctionnalité :

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

Vous pouvez utiliser cette fonction avec un tableau d'objets comme ceci :

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
