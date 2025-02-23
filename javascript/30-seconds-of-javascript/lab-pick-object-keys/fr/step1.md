# Instructions for Picking Object Keys

Pour extraire des paires clé-valeur spécifiques d'un objet, utilisez la fonction `pick(obj, arr)`.

- Passez l'objet en tant que premier argument et un tableau de clés à extraire en tant que deuxième argument.
- La fonction renvoie un nouvel objet ne contenant que les paires clé-valeur correspondant aux clés données.

Voici un exemple d'utilisation de `pick()` :

```js
const pick = (obj, arr) =>
  arr.reduce((acc, curr) => (curr in obj && (acc[curr] = obj[curr]), acc), {});

pick({ a: 1, b: "2", c: 3 }, ["a", "c"]); // { 'a': 1, 'c': 3 }
```

Pour commencer la pratique de codage, ouvrez le Terminal/SSH et tapez `node`.
