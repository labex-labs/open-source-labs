# Comment compter les occurrences en JavaScript

Pour compter le nombre de fois qu'une valeur spécifique apparaît dans un tableau JavaScript, vous pouvez utiliser la méthode `Array.prototype.reduce()`.

Voici comment vous pouvez le faire :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Copiez et collez le code suivant :

```js
const countOccurrences = (arr, val) =>
  arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
```

3. Dans le code ci-dessus, la fonction `countOccurrences` prend deux arguments : le tableau à parcourir et la valeur à compter.
4. La méthode `reduce()` est utilisée pour parcourir chaque élément du tableau et incrémenter un compteur chaque fois que la valeur spécifique est rencontrée.
5. Pour tester la fonction, appelez-la avec un tableau et une valeur, comme ceci :

```js
countOccurrences([1, 1, 2, 1, 2, 3], 1); // 3
```

Cela retournera le nombre de fois que `1` apparaît dans le tableau `[1, 1, 2, 1, 2, 3]`, qui est `3`.
