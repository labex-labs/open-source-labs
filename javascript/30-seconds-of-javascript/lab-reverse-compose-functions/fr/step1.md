# Inversion de la composition de fonctions

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici comment effectuer une composition de fonctions de gauche à droite :

- Utilisez la méthode `Array.prototype.reduce()` pour effectuer une composition de fonctions de gauche à droite.
- La première (la plus à gauche) fonction peut accepter un ou plusieurs arguments, tandis que les fonctions suivantes doivent être unaire.

```js
const composeRight = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

Par exemple :

```js
const add = (x, y) => x + y;
const square = (x) => x * x;
const addAndSquare = composeRight(add, square);
addAndSquare(1, 2); // 9
```
