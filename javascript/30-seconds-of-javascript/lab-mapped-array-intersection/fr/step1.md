# Instructions for Finding Mapped Array Intersection

Pour trouver les éléments communs entre deux tableaux après avoir appliqué une fonction à chaque élément des deux tableaux, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node`.
2. Utilisez le code fourni ci-dessous :

```js
const intersectionBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return [...new Set(a)].filter((x) => s.has(fn(x)));
};
```

3. Dans le code, remplacez `a` et `b` par vos tableaux et `fn` par la fonction que vous voulez appliquer à chaque élément.
4. Exécutez le code pour obtenir le tableau résultant avec les éléments communs.

Exemple :

```js
intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [2.1]
intersectionBy(
  [{ title: "Apple" }, { title: "Orange" }],
  [{ title: "Orange" }, { title: "Melon" }],
  (x) => x.title
); // [{ title: 'Orange' }]
```

Dans le premier exemple, la fonction `Math.floor` est appliquée aux tableaux `[2.1, 1.2]` et `[2.3, 3.4]`, renvoyant l'élément commun `[2.1]`.
Dans le second exemple, la fonction `x => x.title` est appliquée aux tableaux `[{ title: 'Apple' }, { title: 'Orange' }]` et `[{ title: 'Orange' }, { title: 'Melon' }]`, renvoyant l'élément commun `[{ title: 'Orange' }]`.
