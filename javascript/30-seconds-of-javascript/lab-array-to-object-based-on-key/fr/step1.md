# Conversion d'un tableau en objet sur la base d'une clé spécifique

Pour convertir un tableau en objet sur la base d'une clé spécifique et exclure cette clé de chaque valeur, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez `Array.prototype.reduce()` pour créer un objet à partir du tableau fourni.
- Utilisez la déstructuration d'objets pour extraire la valeur de la `clé` donnée et les `données` associées, puis ajoutez la paire clé-valeur à l'objet.

Voici une implémentation d'exemple :

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

Vous pouvez ensuite utiliser la fonction de cette manière :

```js
indexOn(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  "id"
);
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
