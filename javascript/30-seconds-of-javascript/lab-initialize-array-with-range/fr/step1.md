# Fonction pour initialiser un tableau avec une plage

Pour initialiser un tableau avec une plage de nombres, utilisez la fonction suivante :

```js
const initializeArrayWithRange = (end, start = 0, step = 1) => {
  const length = Math.ceil((end - start + 1) / step);
  return Array.from({ length }, (_, i) => i * step + start);
};
```

Cette fonction prend trois arguments : `end` (obligatoire), `start` (optionnel, valeur par défaut est `0`), et `step` (optionnel, valeur par défaut est `1`). Elle renvoie un tableau contenant les nombres dans la plage spécifiée, où `start` et `end` sont inclusifs avec leur différence commune `step`.

Pour utiliser cette fonction, appelez simplement avec les paramètres de plage souhaités :

```js
initializeArrayWithRange(5); // [0, 1, 2, 3, 4, 5]
initializeArrayWithRange(7, 3); // [3, 4, 5, 6, 7]
initializeArrayWithRange(9, 0, 2); // [0, 2, 4, 6, 8]
```

Cette fonction utilise `Array.from()` pour créer un tableau de la longueur souhaitée, puis une fonction de mapping pour remplir le tableau avec les valeurs souhaitées dans la plage donnée. Si vous omettez le deuxième argument, `start`, elle utilisera une valeur par défaut de `0`. Si vous omettez le dernier argument, `step`, elle utilisera une valeur par défaut de `1`.
