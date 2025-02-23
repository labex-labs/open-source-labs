# Comment initialiser un tableau avec une plage inversée en JavaScript

Pour initialiser un tableau avec une plage inversée en JavaScript, utilisez la fonction suivante :

```js
const initializeArrayWithRangeRight = (end, start = 0, step = 1) =>
  Array.from({ length: Math.ceil((end + 1 - start) / step) }).map(
    (v, i, arr) => (arr.length - i - 1) * step + start
  );
```

Cette fonction crée un tableau contenant les nombres de la plage spécifiée dans l'ordre inverse. Les paramètres `start` et `end` sont inclusifs, et le paramètre `step` spécifie la différence commune entre les nombres de la plage.

Pour utiliser la fonction, appelez-la avec les valeurs souhaitées de `end`, `start` et `step` en tant qu'arguments, comme ceci :

```js
initializeArrayWithRangeRight(5); // [5, 4, 3, 2, 1, 0]
initializeArrayWithRangeRight(7, 3); // [7, 6, 5, 4, 3]
initializeArrayWithRangeRight(9, 0, 2); // [8, 6, 4, 2, 0]
```

Si vous omettez l'argument `start`, il prend la valeur par défaut de `0`. Si vous omettez l'argument `step`, il prend la valeur par défaut de `1`.
