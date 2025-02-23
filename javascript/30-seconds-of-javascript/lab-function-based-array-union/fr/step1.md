# Comment trouver l'union de deux tableaux basée sur une fonction

Pour trouver l'union de deux tableaux basée sur une fonction en utilisant Node.js, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node`.
2. Utilisez le code suivant pour créer un `Set` avec toutes les valeurs de `a` et les valeurs de `b` pour lesquelles le comparateur ne trouve pas de correspondance dans `a`, en utilisant `Array.prototype.findIndex()` :

```js
const unionWith = (a, b, comp) =>
  Array.from(
    new Set([...a, ...b.filter((x) => a.findIndex((y) => comp(x, y)) === -1)])
  );
```

3. Appelez la fonction `unionWith` avec trois arguments : le premier tableau, le second tableau et la fonction de comparaison.
4. La fonction renvoie chaque élément qui existe au moins une fois dans l'un des deux tableaux, en utilisant la fonction de comparaison fournie.
5. Voici un exemple d'appel de la fonction `unionWith` :

```js
unionWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
);
// [1, 1.2, 1.5, 3, 0, 3.9]
```

Cela renverra `[1, 1.2, 1.5, 3, 0, 3.9]` comme l'union des deux tableaux.
