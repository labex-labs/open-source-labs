# Composition de fonctions avec des tuyaux

Pour commencer à pratiquer le codage avec des tuyaux, ouvrez le Terminal/SSH et tapez `node`.

La fonction `pipeFunctions` effectue une composition de fonctions de gauche à droite en utilisant `Array.prototype.reduce()` avec l'opérateur de propagation (`...`). La première (la plus à gauche) fonction peut accepter un ou plusieurs arguments, tandis que les fonctions suivantes doivent être unaire.

```js
const pipeFunctions = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

Voici un exemple de manière à utiliser `pipeFunctions` pour créer une nouvelle fonction `multiplyAndAdd5` qui multiplie deux nombres puis ajoute 5 au résultat :

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
const multiplyAndAdd5 = pipeFunctions(multiply, add5);
multiplyAndAdd5(5, 2); // 15
```

Dans cet exemple, `multiplyAndAdd5` est une nouvelle fonction qui prend deux arguments, `5` et `2`, et applique d'abord `multiply` à eux, ce qui donne `10`, puis applique `add5` au résultat, ce qui donne `15`.
