# Comment trouver les valeurs uniques dans un tableau avec JavaScript

Pour trouver toutes les valeurs uniques dans un tableau, vous pouvez suivre ces étapes en JavaScript :

1. Créez un `Set` à partir du tableau donné pour éliminer les valeurs dupliquées.
2. Utilisez l'opérateur de répandage (`...`) pour convertir le `Set` en retournant un tableau.

Voici un extrait de code d'exemple :

```js
const getUniqueValues = (arr) => [...new Set(arr)];
```

Vous pouvez appeler la fonction et lui passer un tableau, comme ceci :

```js
getUniqueValues([1, 2, 2, 3, 4, 4, 5]); // [1, 2, 3, 4, 5]
```

Cela retournera un tableau avec toutes les valeurs uniques du tableau original, sans aucun doublon.
