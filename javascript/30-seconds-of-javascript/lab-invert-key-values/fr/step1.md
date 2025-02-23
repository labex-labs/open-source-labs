# Fonction pour inverser un objet

Pour inverser les paires clé-valeur d'un objet sans modifier l'objet original, utilisez la fonction `invertKeyValues`.

- Appelez la fonction en tapant `invertKeyValues(obj, fn)` dans le Terminal/SSH, où `obj` est l'objet à inverser et `fn` est une fonction optionnelle à appliquer à la clé inversée.

- Les méthodes `Object.keys()` et `Array.prototype.reduce()` sont utilisées pour créer un nouvel objet avec des paires clé-valeur inversées, et si une fonction est fournie, elle est appliquée à chaque clé inversée.

- Si `fn` est omise, la fonction renvoie seulement les clés inversées sans aucune fonction appliquée à elles.

- La fonction renvoie un objet avec chaque valeur inversée étant un tableau de clés responsables de la génération de la valeur inversée.

```js
const invertKeyValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, key) => {
    const val = fn ? fn(obj[key]) : obj[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
```

Utilisation de l'exemple :

```js
invertKeyValues({ a: 1, b: 2, c: 1 }); // { 1: [ 'a', 'c' ], 2: [ 'b' ] }
invertKeyValues({ a: 1, b: 2, c: 1 }, (value) => "group" + value);
// { group1: [ 'a', 'c' ], group2: [ 'b' ] }
```
