# Comment partitionner un tableau en deux en fonction d'une fonction

Pour partitionner un tableau en deux en fonction d'une fonction fournie, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()` pour créer un tableau de deux tableaux.
3. Utilisez `Array.prototype.push()` pour ajouter les éléments pour lesquels `fn` renvoie `true` au premier tableau et les éléments pour lesquels `fn` renvoie `false` au second.

Voici le code que vous pouvez utiliser :

```js
const partition = (arr, fn) =>
  arr.reduce(
    (acc, val, i, arr) => {
      acc[fn(val, i, arr) ? 0 : 1].push(val);
      return acc;
    },
    [[], []]
  );
```

Pour tester ce code, vous pouvez utiliser l'exemple suivant :

```js
const users = [
  { user: "barney", age: 36, active: false },
  { user: "fred", age: 40, active: true }
];
partition(users, (o) => o.active);
// [
//   [{ user: 'fred', age: 40, active: true }],
//   [{ user: 'barney', age: 36, active: false }]
// ]
```

Cela renverra un tableau de deux tableaux, où le premier tableau contient tous les éléments pour lesquels la fonction fournie renvoie `true`, et le second tableau contient tous les éléments pour lesquels la fonction fournie renvoie `false`.
