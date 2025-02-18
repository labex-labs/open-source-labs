# Comment convertir les clés d'un objet en majuscules en JavaScript

Pour convertir toutes les clés d'un objet en majuscules en JavaScript, suivez ces étapes :

1. Utilisez `Object.keys()` pour obtenir un tableau des clés de l'objet.
2. Utilisez `Array.prototype.reduce()` pour mapper le tableau en un objet.
3. Utilisez `String.prototype.toUpperCase()` pour convertir les clés en majuscules.

Voici le code :

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

Pour tester la fonction, vous pouvez l'appeler comme ceci :

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
