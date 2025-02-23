# Comment renommer les clés d'un objet en JavaScript

Pour renommer plusieurs clés d'un objet avec les valeurs fournies, vous pouvez utiliser la fonction `renameKeys`. Voici les étapes à suivre :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer le codage.
2. Utilisez `Object.keys()` en combinaison avec `Array.prototype.reduce()` et l'opérateur de propagation (`...`) pour obtenir les clés de l'objet et les renommer selon `keysMap`.
3. Passez `keysMap` et l'objet (`obj`) en tant qu'arguments à la fonction `renameKeys`.
4. La fonction `renameKeys` renvoie un nouvel objet avec les clés renomées.

Voici un exemple d'utilisation de la fonction `renameKeys` :

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
