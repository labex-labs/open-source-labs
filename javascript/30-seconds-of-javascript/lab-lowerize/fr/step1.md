# Conversion des clés d'un objet en minuscules

Pour convertir toutes les clés d'un objet en minuscules, suivez ces étapes :

1. Ouvrez le Terminal/SSH pour commencer à pratiquer la programmation et tapez `node`.
2. Utilisez `Object.keys()` pour obtenir un tableau des clés de l'objet.
3. Utilisez `Array.prototype.reduce()` pour mapper le tableau sur un objet.
4. Utilisez `String.prototype.toLowerCase()` pour convertir les clés en minuscules.

Voici un exemple de code qui met en œuvre ces étapes :

```js
const lowerize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toLowerCase()] = obj[k];
    return acc;
  }, {});
```

Vous pouvez ensuite appeler la fonction `lowerize()` en passant un objet en argument pour obtenir un nouvel objet avec toutes les clés en minuscules. Par exemple :

```js
lowerize({ Name: "John", Age: 22 }); // { name: 'John', age: 22 }
```
