# Comment congeler complètement un objet en JavaScript

Pour congeler complètement un objet en JavaScript, suivez ces étapes :

1. Utilisez `Object.keys()` pour obtenir toutes les propriétés de l'objet passé.
2. Itérez sur les propriétés à l'aide de `Array.prototype.forEach()`.
3. Appelez `Object.freeze()` de manière récursive sur toutes les propriétés qui sont des objets, en appliquant `deepFreeze()` si nécessaire.
4. Enfin, utilisez `Object.freeze()` pour congeler l'objet donné.

Voici le code :

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

Vous pouvez tester l'objet complètement congelé à l'aide du code suivant :

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // interdit
val[1][0] = 4; // également interdit
```

Le code ci-dessus générera une erreur car l'objet `val` est complètement congelé et ne peut pas être modifié.
