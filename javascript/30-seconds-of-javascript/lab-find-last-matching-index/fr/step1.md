# Comment trouver l'index du dernier élément correspondant dans un tableau en utilisant JavaScript

Pour trouver l'index du dernier élément qui correspond à une certaine condition dans un tableau JavaScript, utilisez la fonction `findLastIndex`. Voici comment l'utiliser :

```js
const findLastIndex = (arr, fn) =>
  (arr
    .map((val, i) => [i, val])
    .filter(([i, val]) => fn(val, i, arr))
    .pop() || [-1])[0];
```

La fonction `findLastIndex` prend deux arguments : le tableau à parcourir et une fonction pour tester chaque élément. Voici comment elle fonctionne :

1. Utilisez `Array.prototype.map()` pour créer un nouveau tableau de paires `[index, valeur]`.
2. Utilisez `Array.prototype.filter()` pour supprimer les éléments du tableau qui ne correspondent pas à la condition fournie par la fonction `fn`.
3. Utilisez `Array.prototype.pop()` pour obtenir le dernier élément du tableau filtré.
4. Si le tableau filtré est vide, renvoyez `-1`.

Voici un exemple d'utilisation de `findLastIndex` :

```js
findLastIndex([1, 2, 3, 4], (n) => n % 2 === 1); // 2 (index de la valeur 3)
findLastIndex([1, 2, 3, 4], (n) => n === 5); // -1 (valeur par défaut lorsqu'aucun élément n'est trouvé)
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
