# Instructions pour extraire des valeurs d'un tableau d'objets

Pour extraire des valeurs d'un tableau d'objets, vous pouvez suivre les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.map()` pour mapper le tableau d'objets à la valeur d'une `clé` spécifiée pour chaque objet.
3. Implémentez la fonction suivante :

```js
const pluck = (arr, key) => arr.map((i) => i[key]);
```

4. Testez la fonction avec un exemple de tableau d'objets :

```js
const simpsons = [
  { name: "lisa", age: 8 },
  { name: "homer", age: 36 },
  { name: "marge", age: 34 },
  { name: "bart", age: 10 }
];
pluck(simpsons, "age"); // [8, 36, 34, 10]
```

Cela renverra un tableau de valeurs correspondant à la `clé` spécifiée à partir du tableau d'objets.
