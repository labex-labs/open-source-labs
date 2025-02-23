# Comment diviser un tableau en N morceaux

Pour diviser un tableau en `n` tableaux plus petits, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Math.ceil()` et `Array.prototype.length` pour calculer la taille de chaque morceau.
3. Utilisez `Array.from()` pour créer un nouveau tableau de taille `n`.
4. Utilisez `Array.prototype.slice()` pour mapper chaque élément du nouveau tableau à un morceau de longueur `size`.
5. Si le tableau original ne peut pas être divisé en parties égales, le dernier morceau contiendra les éléments restants.

Voici une implémentation de l'exemple de la fonction `chunkIntoN` en JavaScript :

```js
const chunkIntoN = (arr, n) => {
  const size = Math.ceil(arr.length / n);
  return Array.from({ length: n }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
};
```

Vous pouvez utiliser cette fonction pour diviser un tableau en `n` morceaux en passant le tableau et le nombre de morceaux souhaité en arguments. Par exemple :

```js
chunkIntoN([1, 2, 3, 4, 5, 6, 7], 4); // [[1, 2], [3, 4], [5, 6], [7]]
```
