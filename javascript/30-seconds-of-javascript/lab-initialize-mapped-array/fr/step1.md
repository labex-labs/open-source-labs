# Initialiser un tableau mappé en JavaScript

Pour initialiser un tableau mappé en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le constructeur `Array()` pour créer un tableau de la longueur souhaitée.
3. Utilisez `Array.prototype.fill()` pour remplir le tableau avec des valeurs `null`.
4. Utilisez `Array.prototype.map()` pour remplir le tableau avec les valeurs souhaitées, en utilisant la fonction fournie, `mapFn`.
5. Omettez le deuxième argument, `mapFn`, pour mapper chaque élément à son index.

Voici un extrait de code d'exemple :

```js
const initializeMappedArray = (n, mapFn = (_, i) => i) =>
  Array(n).fill(null).map(mapFn);
```

Vous pouvez utiliser la fonction `initializeMappedArray` pour créer un tableau mappé avec les valeurs souhaitées :

```js
initializeMappedArray(5); // [0, 1, 2, 3, 4]
initializeMappedArray(5, (i) => `item ${i + 1}`);
// ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
```
