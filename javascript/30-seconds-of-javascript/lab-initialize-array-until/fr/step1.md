# Comment initialiser un tableau jusqu'à ce qu'une condition soit remplie

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici les étapes pour initialiser et remplir un tableau avec des valeurs générées par une fonction jusqu'à ce qu'une certaine condition soit remplie :

1. Créez un tableau vide `arr`, une variable d'index `i` et un élément `el`.
2. Utilisez une boucle `do...while` pour ajouter des éléments au tableau en utilisant la fonction `mapFn` jusqu'à ce que la fonction `conditionFn` retourne `true` pour l'index `i` et l'élément `el` donnés.
3. La fonction `conditionFn` prend trois arguments : l'index actuel, l'élément précédent et le tableau lui-même.
4. La fonction `mapFn` prend trois arguments : l'index actuel, l'élément actuel et le tableau lui-même.

Voici le code :

```js
const initializeArrayUntil = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = undefined;
  do {
    el = mapFn(i, el, arr);
    arr.push(el);
    i++;
  } while (!conditionFn(i, el, arr));
  return arr;
};
```

Pour utiliser la fonction `initializeArrayUntil`, fournissez deux fonctions en tant qu'arguments :

```js
initializeArrayUntil(
  (i, val) => val > 10, //conditionFn
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2]) //mapFn
); // [1, 1, 2, 3, 5, 8, 13]
```

Ce code initialise un tableau avec la suite de Fibonacci jusqu'au premier nombre supérieur à 10. La fonction `conditionFn` vérifie si la valeur actuelle est supérieure à 10, et la fonction `mapFn` génère le prochain nombre de la suite.
