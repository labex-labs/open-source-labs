# Comment itérer sur les propriétés propres d'un objet en JavaScript

Pour itérer sur les propriétés propres d'un objet et pratiquer la programmation, suivez ces étapes :

1. Ouvrez le Terminal ou SSH.
2. Tapez `node` pour démarrer une nouvelle session Node.js.
3. Utilisez la méthode `Object.keys()` pour récupérer un tableau des propriétés propres de l'objet.
4. Utilisez la méthode `Array.prototype.forEach()` pour parcourir chaque propriété et exécuter une fonction fournie.
5. La fonction fournie devrait accepter trois arguments : la valeur de la propriété, la clé de la propriété et l'objet lui-même.
6. Utilisez la fonction `forOwn()` avec l'objet et la fonction fournie pour itérer sur les propriétés de l'objet.

Voici un extrait de code d'exemple :

```js
const forOwn = (obj, fn) =>
  Object.keys(obj).forEach((key) => fn(obj[key], key, obj));

forOwn({ foo: "bar", a: 1 }, (v) => console.log(v)); // 'bar', 1
```

Ce code affichera les valeurs des propriétés `foo` et `a` dans la console.
