# Comment diviser un tableau en morceaux d'une taille spécifique

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Pour diviser un tableau en tableaux plus petits d'une taille spécifiée, suivez ces étapes :

1. Utilisez `Array.from()` pour créer un nouveau tableau qui correspond au nombre de morceaux qui seront produits.
2. Utilisez `Array.prototype.slice()` pour mapper chaque élément du nouveau tableau à un morceau de longueur `size`.
3. Si le tableau original ne peut pas être divisé en parties égales, le dernier morceau contiendra les éléments restants.

Voici un extrait de code d'exemple :

```js
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
```

Vous pouvez utiliser cette fonction en passant le tableau que vous voulez diviser et la taille souhaitée des morceaux. Par exemple :

```js
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```
