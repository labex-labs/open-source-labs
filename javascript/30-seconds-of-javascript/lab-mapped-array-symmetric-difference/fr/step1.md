# Différence symétrique d'un tableau mappé

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction renvoie la différence symétrique entre deux tableaux, après avoir appliqué la fonction fournie à chaque élément des deux tableaux. Voici comment elle fonctionne :

- Créez un `Set` à partir de chaque tableau pour obtenir les valeurs uniques de chacun d'eux après avoir appliqué `fn` à leurs éléments.
- Utilisez `Array.prototype.filter()` sur chacun d'eux pour ne conserver que les valeurs qui ne sont pas contenues dans l'autre.

Voici le code de la fonction `symmetricDifferenceBy` :

```js
const symmetricDifferenceBy = (a, b, fn) => {
  const sA = new Set(a.map((v) => fn(v))),
    sB = new Set(b.map((v) => fn(v)));
  return [
    ...a.filter((x) => !sB.has(fn(x))),
    ...b.filter((x) => !sA.has(fn(x)))
  ];
};
```

Vous pouvez utiliser `symmetricDifferenceBy` comme ceci :

```js
symmetricDifferenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [ 1.2, 3.4 ]
symmetricDifferenceBy(
  [{ id: 1 }, { id: 2 }, { id: 3 }],
  [{ id: 1 }, { id: 2 }, { id: 4 }],
  (i) => i.id
);
// [{ id: 3 }, { id: 4 }]
```
