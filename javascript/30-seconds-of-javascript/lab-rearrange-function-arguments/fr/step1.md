# Comment réordonner les arguments de fonction en JavaScript

Pour réordonner les arguments de fonction en JavaScript, vous pouvez utiliser la fonction `rearg()`. Tout d'abord, créez une fonction qui invoque la fonction fournie avec ses arguments arrangés selon les index spécifiés. Vous pouvez utiliser `Array.prototype.map()` pour réordonner les arguments en fonction des `indexes`. Ensuite, utilisez l'opérateur de propagation (`...`) pour passer les arguments transformés à `fn`.

Voici un exemple de manière d'utiliser la fonction `rearg()` :

```js
const rearg =
  (fn, indexes) =>
  (...args) =>
    fn(...indexes.map((i) => args[i]));
```

Dans cet exemple, nous utilisons `rearg()` pour créer une nouvelle fonction qui réarrange les arguments d'une autre fonction.

```js
var rearged = rearg(
  function (a, b, c) {
    return [a, b, c];
  },
  [2, 0, 1]
);
rearged("b", "c", "a"); // ['a', 'b', 'c']
```

Dans le code ci-dessus, nous créons une nouvelle fonction `rearged` qui réarrange les arguments de la fonction `function(a, b, c) { return [a, b, c]; }`. L'argument `indexes` spécifie l'ordre dans lequel les arguments doivent être réarrangés. Dans ce cas, nous voulons que le troisième argument vienne en premier, le premier argument vienne en second et le second argument vienne en troisième. Lorsque nous appelons `rearged('b', 'c', 'a')`, il renvoie `['a', 'b', 'c']`, qui est le résultat de l'appel de la fonction d'origine avec les arguments réarrangés.
