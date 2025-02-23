# Comment attribuer des valeurs par défaut aux propriétés d'un objet

Pour attribuer des valeurs par défaut à toutes les propriétés d'un objet qui sont `undefined`, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.assign()` pour créer un nouvel objet vide et copier l'objet original pour conserver l'ordre des clés.
3. Utilisez `Array.prototype.reverse()` et l'opérateur de propagation (`...`) pour combiner les valeurs par défaut de gauche à droite.
4. Enfin, utilisez `obj` à nouveau pour écraser les propriétés qui avaient une valeur initialement.

Voici un extrait de code d'exemple :

```js
const defaults = (obj, ...defs) =>
  Object.assign({}, obj, ...defs.reverse(), obj);

defaults({ a: 1 }, { b: 2 }, { b: 6 }, { a: 3 }); // { a: 1, b: 2 }
```

Ce fragment de code retournera un objet qui a des valeurs par défaut pour toutes les propriétés qui étaient indéfinies dans l'objet original.
