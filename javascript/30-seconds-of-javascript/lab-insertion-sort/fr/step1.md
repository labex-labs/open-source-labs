# Tri par insertion en JavaScript

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Cet algorithme trie un tableau de nombres en utilisant la méthode de tri par insertion. Suivez ces étapes pour implémenter cet algorithme :

1. Utilisez `Array.prototype.reduce()` pour itérer sur tous les éléments du tableau donné.
2. Si la `length` de l'accumulateur est `0`, ajoutez l'élément actuel à celui-ci.
3. Utilisez `Array.prototype.some()` pour itérer sur les résultats dans l'accumulateur jusqu'à trouver la position correcte.
4. Utilisez `Array.prototype.splice()` pour insérer l'élément actuel dans l'accumulateur.

Voici le code pour implémenter le tri par insertion en JavaScript :

```js
const insertionSort = (arr) =>
  arr.reduce((acc, x) => {
    if (!acc.length) return [x];
    acc.some((y, j) => {
      if (x <= y) {
        acc.splice(j, 0, x);
        return true;
      }
      if (x > y && j === acc.length - 1) {
        acc.splice(j + 1, 0, x);
        return true;
      }
      return false;
    });
    return acc;
  }, []);
```

Vous pouvez tester l'algorithme avec le code suivant :

```js
insertionSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
