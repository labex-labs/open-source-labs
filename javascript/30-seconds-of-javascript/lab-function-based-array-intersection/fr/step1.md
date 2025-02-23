# Comment trouver l'intersection d'ensembles basée sur une fonction en utilisant JavaScript

Pour trouver les éléments qui existent dans les deux tableaux en fonction d'une fonction de comparaison fournie, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez `Array.prototype.filter()` et `Array.prototype.findIndex()` en combinaison avec la fonction de comparaison fournie pour déterminer les valeurs communes.

   ```js
   const intersectionWith = (a, b, comp) =>
     a.filter((x) => b.findIndex((y) => comp(x, y)) !== -1);
   ```

3. Appelez la fonction `intersectionWith()` avec les deux tableaux et la fonction de comparaison en tant qu'arguments.

   ```js
   intersectionWith(
     [1, 1.2, 1.5, 3, 0],
     [1.9, 3, 0, 3.9],
     (a, b) => Math.round(a) === Math.round(b)
   ); // [1.5, 3, 0]
   ```

Cela retournera un tableau contenant les valeurs communes entre les deux tableaux, en fonction de la fonction de comparaison fournie.
