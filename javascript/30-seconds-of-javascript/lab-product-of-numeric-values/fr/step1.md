# Comment calculer le produit de valeurs numériques en JavaScript

Pour calculer le produit de deux ou plusieurs nombres ou tableaux en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.reduce()` pour multiplier chaque valeur par un accumulateur, qui doit être initialisé avec une valeur de `1`.
3. Définissez une fonction appelée `prod` qui prend un nombre quelconque d'arguments en utilisant l'opérateur de propagation (`...`). Dans la fonction, appliquez la méthode `reduce()` au tableau de arguments en diffusion.
4. La fonction renvoie le résultat de la multiplication.

Voici un exemple de manière d'utiliser la fonction `prod` :

```js
const prod = (...arr) => [...arr].reduce((acc, val) => acc * val, 1);

prod(1, 2, 3, 4); // 24
prod(...[1, 2, 3, 4]); // 24
```

Dans l'exemple ci-dessus, `prod(1, 2, 3, 4)` et `prod(...[1, 2, 3, 4])` renvoient tous les deux `24`.
