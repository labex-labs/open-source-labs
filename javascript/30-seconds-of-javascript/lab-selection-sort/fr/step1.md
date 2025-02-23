# Algorithme de tri par sélection

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

La fonction suivante trie un tableau de nombres en utilisant l'algorithme de tri par sélection :

```js
const selectionSort = (arr) => {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    const min = a
      .slice(i + 1)
      .reduce((acc, val, j) => (val < a[acc] ? j + i + 1 : acc), i);
    if (min !== i) [a[i], a[min]] = [a[min], a[i]];
  }
  return a;
};
```

Pour utiliser la fonction, passez un tableau de nombres à `selectionSort()`, comme ceci :

```js
selectionSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```

La fonction fonctionne en clonant le tableau original à l'aide de l'opérateur de propagation (`...`). Elle itère ensuite sur le tableau à l'aide d'une boucle `for`. En utilisant `Array.prototype.slice()` et `Array.prototype.reduce()`, elle trouve l'index de l'élément minimum dans le sous-tableau à droite de l'index actuel. Si nécessaire, elle effectue un échange.
