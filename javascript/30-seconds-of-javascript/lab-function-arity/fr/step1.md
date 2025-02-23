# Comment créer une fonction avec un nombre spécifique d'arguments

Pour créer une fonction qui accepte un nombre spécifique d'arguments et ignore tout argument supplémentaire, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez le code suivant pour créer votre fonction :

```js
const ary =
  (fn, n) =>
  (...args) =>
    fn(...args.slice(0, n));
```

3. Appelez la fonction que vous venez de créer, `ary`, avec deux arguments : la fonction pour laquelle vous voulez limiter les arguments (`fn`) et le nombre d'arguments auquel vous voulez la limiter (`n`).

4. Maintenant, vous pouvez utiliser la nouvelle fonction pour limiter le nombre d'arguments de n'importe quelle fonction que vous voulez. Pour ce faire, appelez votre nouvelle fonction avec l'opérateur de répétition (`...`) et les arguments que vous voulez limiter.

Voici un exemple de manière à utiliser votre nouvelle fonction :

```js
const firstTwoMax = ary(Math.max, 2);
[[2, 6, "a"], [6, 4, 8], [10]].map((x) => firstTwoMax(...x)); // [6, 6, 10]
```

Dans cet exemple, `firstTwoMax` est une nouvelle fonction qui limite la fonction `Math.max` à n'accepter que les deux premiers arguments. La méthode `map` est utilisée pour appliquer la nouvelle fonction à chaque tableau de l'array externe, renvoyant le maximum des deux premiers éléments de chaque tableau interne.
