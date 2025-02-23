# Fonction de fusion d'objets

Pour fusionner deux ou plusieurs objets, suivez les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.
2. Utilisez `Array.prototype.reduce()` avec `Object.keys()` pour itérer sur tous les objets et les clés.
3. Utilisez `Object.prototype.hasOwnProperty()` et `Array.prototype.concat()` pour ajouter les valeurs pour les clés existant dans plusieurs objets.
4. Utilisez le extrait de code donné pour créer un nouvel objet à partir de la combinaison de deux ou plusieurs objets.

```js
const merge = (...objs) =>
  [...objs].reduce(
    (acc, obj) =>
      Object.keys(obj).reduce((a, k) => {
        acc[k] = acc.hasOwnProperty(k)
          ? [].concat(acc[k]).concat(obj[k])
          : obj[k];
        return acc;
      }, {}),
    {}
  );
```

Par exemple, considérez les objets suivants :

```js
const object = {
  a: [{ x: 2 }, { y: 4 }],
  b: 1
};
const other = {
  a: { z: 3 },
  b: [2, 3],
  c: "foo"
};
```

Lorsque vous fusionnez ces deux objets à l'aide de la fonction `merge()`, vous obtenez le résultat suivant :

```js
merge(object, other);
// { a: [ { x: 2 }, { y: 4 }, { z: 3 } ], b: [ 1, 2, 3 ], c: 'foo' }
```
