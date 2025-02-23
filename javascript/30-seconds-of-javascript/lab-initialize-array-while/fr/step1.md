# Comment initialiser et remplir un tableau avec une boucle while en JavaScript

Pour commencer à pratiquer la programmation en JavaScript, ouvrez le Terminal/SSH et tapez `node`.

La fonction `initializeArrayWhile` initialise et remplit un tableau avec des valeurs générées par une fonction tant qu'une condition est satisfaite. Voici comment elle fonctionne :

1. Créez un tableau vide appelé `arr`, une variable d'index appelée `i` et un élément appelé `el`.
2. Utilisez une boucle `while` pour ajouter des éléments au tableau à l'aide de la fonction `mapFn`, tant que la fonction `conditionFn` renvoie `true` pour l'index `i` et l'élément `el` donnés.
3. La fonction `conditionFn` prend trois arguments : l'index actuel, l'élément précédent et le tableau lui-même.
4. La fonction `mapFn` prend trois arguments : l'index actuel, l'élément actuel et le tableau lui-même.
5. La fonction `initializeArrayWhile` renvoie le tableau.

Voici le code :

```js
const initializeArrayWhile = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = mapFn(i, undefined, arr);
  while (conditionFn(i, el, arr)) {
    arr.push(el);
    i++;
    el = mapFn(i, el, arr);
  }
  return arr;
};
```

Vous pouvez utiliser la fonction `initializeArrayWhile` pour initialiser et remplir un tableau avec des valeurs. Par exemple :

```js
initializeArrayWhile(
  (i, val) => val < 10,
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2])
); // [1, 1, 2, 3, 5, 8]
```
