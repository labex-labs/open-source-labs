# Comment déplier un objet en JavaScript

Pour déplier un objet avec des chemins pour les clés en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez `Array.prototype.reduce()` imbriquée pour convertir le chemin plat en un nœud feuille.

3. Utilisez `String.prototype.split()` pour diviser chaque clé avec un délimiteur de point et `Array.prototype.reduce()` pour ajouter des objets contre les clés.

4. Si l'accumulateur actuel contient déjà une valeur pour une clé particulière, renvoyez sa valeur comme le prochain accumulateur.

5. Sinon, ajoutez la paire clé-valeur appropriée à l'objet accumulateur et renvoyez la valeur comme l'accumulateur.

Voici le code pour la fonction `unflattenObject` :

```js
const unflattenObject = (obj) =>
  Object.keys(obj).reduce((res, k) => {
    k.split(".").reduce(
      (acc, e, i, keys) =>
        acc[e] ||
        (acc[e] = isNaN(Number(keys[i + 1]))
          ? keys.length - 1 === i
            ? obj[k]
            : {}
          : []),
      res
    );
    return res;
  }, {});
```

Vous pouvez utiliser la fonction `unflattenObject` pour déplier un objet en JavaScript :

```js
unflattenObject({ "a.b.c": 1, d: 1 }); // { a: { b: { c: 1 } }, d: 1 }
unflattenObject({ "a.b": 1, "a.c": 2, d: 3 }); // { a: { b: 1, c: 2 }, d: 3 }
unflattenObject({ "a.b.0": 8, d: 3 }); // { a: { b: [ 8 ] }, d: 3 }
```
