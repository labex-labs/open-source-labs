# Parcours des clés d'un objet

Pour générer une liste de toutes les clés d'un objet donné, utilisez les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Définissez une fonction génératrice appelée `walk` qui prend un objet et un tableau de clés. Utilisez la récursivité pour parcourir toutes les clés de l'objet.

3. À l'intérieur de la fonction `walk`, utilisez une boucle `for...of` et `Object.keys()` pour itérer sur les clés de l'objet.

4. Utilisez `typeof` pour vérifier si chaque valeur dans l'objet donné est elle-même un objet. Si la valeur est un objet, utilisez l'expression `yield*` pour déléguer de manière récursive à la même fonction génératrice, `walk`, en ajoutant la `clé` actuelle au tableau de clés.

5. Sinon, `yield` un tableau de clés représentant le chemin actuel et la valeur de la `clé` donnée.

6. Utilisez l'expression `yield*` pour déléguer à la fonction génératrice `walk`.

Voici le code :

```js
const walkThrough = function* (obj) {
  const walk = function* (x, previous = []) {
    for (let key of Object.keys(x)) {
      if (typeof x[key] === "object") yield* walk(x[key], [...previous, key]);
      else yield [[...previous, key], x[key]];
    }
  };
  yield* walk(obj);
};
```

Pour tester le code, créez un objet et utilisez la fonction `walkThrough` pour générer une liste de toutes ses clés :

```js
const obj = {
  a: 10,
  b: 20,
  c: {
    d: 10,
    e: 20,
    f: [30, 40]
  },
  g: [
    {
      h: 10,
      i: 20
    },
    {
      j: 30
    },
    40
  ]
};
[...walkThrough(obj)];
/*
[
  [['a'], 10],
  [['b'], 20],
  [['c', 'd'], 10],
  [['c', 'e'], 20],
  [['c', 'f', '0'], 30],
  [['c', 'f', '1'], 40],
  [['g', '0', 'h'], 10],
  [['g', '0', 'i'], 20],
  [['g', '1', 'j'], 30],
  [['g', '2'], 40]
]
*/
```
