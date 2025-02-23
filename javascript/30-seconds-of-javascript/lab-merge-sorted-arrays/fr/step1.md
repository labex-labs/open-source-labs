# Instructions for Merging Sorted Arrays in JavaScript

Pour fusionner deux tableaux triés en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez l'opérateur de propagation (`...`) pour cloner les deux tableaux donnés.
3. Utilisez `Array.from()` pour créer un tableau de la longueur appropriée en fonction des tableaux donnés.
4. Utilisez `Array.prototype.shift()` pour remplir le nouveau tableau créé avec les éléments supprimés des tableaux clonés.

Voici un extrait de code d'exemple pour fusionner deux tableaux triés :

```js
const mergeSortedArrays = (a, b) => {
  const _a = [...a],
    _b = [...b];
  return Array.from({ length: _a.length + _b.length }, () => {
    if (!_a.length) return _b.shift();
    else if (!_b.length) return _a.shift();
    else return _a[0] > _b[0] ? _b.shift() : _a.shift();
  });
};

console.log(mergeSortedArrays([1, 4, 5], [2, 3, 6])); // Sortie : [1, 2, 3, 4, 5, 6]
```

Dans le code ci-dessus, la fonction `mergeSortedArrays` prend deux tableaux triés en arguments et renvoie le tableau fusionné en suivant les étapes ci-dessus. La sortie du code d'exemple est `[1, 2, 3, 4, 5, 6]`.
