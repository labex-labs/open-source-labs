# Filtrer des objets selon une condition et des clés

Pour filtrer un tableau d'objets selon une condition tout en éliminant également les clés non spécifiées, utilisez la fonction `reducedFilter()`.

Voici les étapes à suivre :

1. Utilisez `Array.prototype.filter()` pour filtrer le tableau selon le prédicat `fn` de sorte qu'il renvoie les objets pour lesquels la condition a retourné une valeur vraie.

2. Utilisez `Array.prototype.map()` sur le tableau filtré pour renvoyer le nouvel objet.

3. Utilisez `Array.prototype.reduce()` pour éliminer les clés qui n'ont pas été fournies en tant qu'argument `keys`.

```js
const reducedFilter = (data, keys, fn) =>
  data.filter(fn).map((el) =>
    keys.reduce((acc, key) => {
      acc[key] = el[key];
      return acc;
    }, {})
  );
```

Voici un exemple d'utilisation de la fonction `reducedFilter()` :

```js
const data = [
  {
    id: 1,
    name: "john",
    age: 24
  },
  {
    id: 2,
    name: "mike",
    age: 50
  }
];

reducedFilter(data, ["id", "name"], (item) => item.age > 24);
// Sortie : [{ id: 2, name:'mike'}]
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
