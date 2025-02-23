# Remove Keys from Object

Pour supprimer des clés spécifiques d'un objet, utilisez la fonction `omit` qui prend un objet et un tableau de clés à supprimer.

- La méthode `Object.keys()` est utilisée pour obtenir toutes les clés de l'objet
- La méthode `Array.prototype.filter()` est ensuite utilisée pour supprimer les clés spécifiées de la liste de clés
- Enfin, `Array.prototype.reduce()` est utilisée pour créer un nouvel objet avec les paires clé-valeur restantes

```js
const omit = (obj, keysToRemove) =>
  Object.keys(obj)
    .filter((key) => !keysToRemove.includes(key))
    .reduce((newObj, key) => {
      newObj[key] = obj[key];
      return newObj;
    }, {});
```

Exemple d'utilisation :

```js
omit({ a: 1, b: "2", c: 3 }, ["b"]); // { 'a': 1, 'c': 3 }
```
