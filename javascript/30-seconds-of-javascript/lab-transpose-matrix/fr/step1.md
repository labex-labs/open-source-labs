# Transpose a Matrix in JavaScript

Pour transposer un tableau bidimensionnel en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.map()` pour créer la transposée du tableau bidimensionnel donné. La méthode `map()` crée un nouveau tableau avec les résultats de l'appel d'une fonction fournie sur chaque élément du tableau.
3. La fonction fournie devrait prendre deux arguments : l'élément actuel du tableau et son index. Dans ce cas, nous avons seulement besoin de l'index pour créer la transposée.
4. Utilisez l'index pour accéder aux éléments correspondants dans chaque ligne du tableau bidimensionnel et créez un nouveau tableau avec ces éléments. Ce sera la nouvelle ligne dans le tableau transposé.
5. Répétez l'étape précédente pour chaque colonne dans le tableau bidimensionnel pour créer le tableau transposé complet.

Voici le code pour transposer un tableau bidimensionnel en JavaScript :

```js
const transpose = (arr) => arr[0].map((col, i) => arr.map((row) => row[i]));

transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]);
// [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
```
