# JavaScript Function to Group Array Elements

Pour regrouper les éléments dans des tableaux, vous pouvez utiliser la fonction `zipWith`.

Voici comment elle fonctionne :

- La fonction prend un nombre illimité de tableaux en arguments.
- Elle vérifie si le dernier argument est une fonction.
- Elle utilise `Math.max()` pour trouver la longueur du plus long tableau.
- Elle crée un nouveau tableau d'éléments regroupés à l'aide de `Array.from()` et d'une fonction de mapping.
- Si les longueurs des tableaux d'arguments varient, `undefined` est utilisé là où aucune valeur n'a été trouvée.
- La fonction est appelée avec les éléments de chaque groupe.

Voici un exemple d'utilisation de la fonction `zipWith` :

```js
zipWith([1, 2], [10, 20], [100, 200], (a, b, c) => a + b + c); // [111, 222]
zipWith(
  [1, 2, 3],
  [10, 20],
  [100, 200],
  (a, b, c) =>
    (a != null ? a : "a") + (b != null ? b : "b") + (c != null ? c : "c")
); // [111, 222, '3bc']
```

Pour utiliser la fonction `zipWith`, ouvrez le Terminal/SSH et tapez `node`.
