# Comment fusionner profondément des objets en JavaScript

Pour fusionner profondément deux objets en JavaScript, vous pouvez utiliser la fonction `deepMerge`. Cette fonction prend deux objets et une fonction en arguments. La fonction est utilisée pour gérer les clés présentes dans les deux objets.

Voici comment fonctionne la fonction `deepMerge` :

1. Utilisez `Object.keys()` pour obtenir les clés des deux objets, créez un `Set` à partir d'elles et utilisez l'opérateur de répétition (`...`) pour créer un tableau de toutes les clés uniques.
2. Utilisez `Array.prototype.reduce()` pour ajouter chaque clé unique à l'objet, en utilisant `fn` pour combiner les valeurs des deux objets donnés.

Voici le code de la fonction `deepMerge` :

```js
const deepMerge = (a, b, fn) =>
  [...new Set([...Object.keys(a), ...Object.keys(b)])].reduce(
    (acc, key) => ({ ...acc, [key]: fn(key, a[key], b[key]) }),
    {}
  );
```

Pour utiliser la fonction `deepMerge`, appelez-la avec deux objets et une fonction. Voici un exemple :

```js
deepMerge(
  { a: true, b: { c: [1, 2, 3] } },
  { a: false, b: { d: [1, 2, 3] } },
  (key, a, b) => (key === "a" ? a && b : Object.assign({}, a, b))
);
// { a: false, b: { c: [ 1, 2, 3 ], d: [ 1, 2, 3 ] } }
```

Dans cet exemple, la fonction `deepMerge` est utilisée pour fusionner deux objets. L'objet résultant a les valeurs des deux objets fusionnées ensemble.
