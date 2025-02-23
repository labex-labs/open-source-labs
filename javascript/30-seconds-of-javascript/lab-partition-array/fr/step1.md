# Algorithme de partitionnement de tableau

Pour partitionner un tableau, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Appliquez la fonction `fn` fournie à chaque valeur du tableau `arr` donné.
3. Divisez le tableau chaque fois que `fn` renvoie une nouvelle valeur.
4. Utilisez `Array.prototype.reduce()` pour créer un objet accumulateur qui contient le tableau résultant et la dernière valeur renvoyée par `fn`.
5. Utilisez `Array.prototype.push()` pour ajouter chaque valeur de `arr` à la partition appropriée dans le tableau accumulateur.
6. Retournez le tableau résultant.

Voici la mise en œuvre du code :

```js
const partitionBy = (arr, fn) =>
  arr.reduce(
    ({ res, last }, v, i, a) => {
      const next = fn(v, i, a);
      if (next !== last) res.push([v]);
      else res[res.length - 1].push(v);
      return { res, last: next };
    },
    { res: [] }
  ).res;
```

Utilisation de l'exemple :

```js
const numbers = [1, 1, 3, 3, 4, 5, 5, 5];
partitionBy(numbers, (n) => n % 2 === 0); // [[1, 1, 3, 3], [4], [5, 5, 5]]
partitionBy(numbers, (n) => n); // [[1, 1], [3, 3], [4], [5, 5, 5]]
```
