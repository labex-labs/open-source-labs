# Comment composer des fonctions en JavaScript

Pour commencer à pratiquer la programmation en utilisant la composition de fonctions en JavaScript, ouvrez le Terminal/SSH et tapez `node`.

Voici un exemple de la manière de réaliser une composition de fonctions de droite à gauche en JavaScript :

1. Utilisez `Array.prototype.reduce()` pour effectuer une composition de fonctions de droite à gauche.
2. La dernière (la plus à droite) fonction peut accepter un ou plusieurs arguments ; les fonctions restantes doivent être unaires.
3. Définissez la fonction `compose` qui prendra un nombre quelconque de fonctions en arguments et renverra une nouvelle fonction qui les compose.
4. Appelez la fonction `compose` avec les fonctions souhaitées dans l'ordre souhaité.
5. Appelez la nouvelle fonction composée avec tous les arguments nécessaires.

```js
const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args))
  );
```

Par exemple, disons que nous avons deux fonctions :

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
```

Nous pouvons composer ces fonctions en utilisant `compose` :

```js
const multiplyAndAdd5 = compose(add5, multiply);
```

Maintenant, nous pouvons appeler `multiplyAndAdd5` avec les arguments souhaités :

```js
multiplyAndAdd5(5, 2); // 15
```
