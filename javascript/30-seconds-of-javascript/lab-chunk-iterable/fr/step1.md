# Découper un itérable

Pour découper un itérable en tableaux plus petits d'une taille spécifiée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez une boucle `for...of` sur l'itérable donné, en utilisant `Array.prototype.push()` pour ajouter chaque nouvelle valeur au `chunk` actuel.
3. Vérifiez si le `chunk` actuel est de la `size` souhaitée en utilisant `Array.prototype.length` et `yield` la valeur si c'est le cas.
4. Vérifiez le dernier `chunk` en utilisant `Array.prototype.length` et `yield` s'il n'est pas vide.
5. Utilisez le code suivant :

```js
const chunkify = function* (itr, size) {
  let chunk = [];
  for (const v of itr) {
    chunk.push(v);
    if (chunk.length === size) {
      yield chunk;
      chunk = [];
    }
  }
  if (chunk.length) yield chunk;
};
```

6. Utilisez ce code pour tester la fonction :

```js
const x = new Set([1, 2, 1, 3, 4, 1, 2, 5]);
[...chunkify(x, 2)]; // [[1, 2], [3, 4], [5]]
```
