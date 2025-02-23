# Comment négater une fonction prédicat en JavaScript

Pour négater une fonction prédicat en JavaScript, vous pouvez utiliser l'opérateur `!`. Pour ce faire, vous pouvez créer une fonction de haut niveau appelée `negate` qui prend une fonction prédicat et applique l'opérateur `!` à celle-ci avec ses arguments. Voici un exemple de mise en œuvre de `negate` :

```js
const negate =
  (func) =>
  (...args) =>
    !func(...args);
```

Vous pouvez ensuite utiliser `negate` pour négater n'importe quelle fonction prédicat. Voici un exemple de manière à utiliser `negate` pour filtrer les nombres pairs dans un tableau :

```js
const isEven = (n) => n % 2 === 0;
const isOdd = negate(isEven);

[1, 2, 3, 4, 5, 6].filter(isOdd); // [ 1, 3, 5 ]
```

Dans cet exemple, `isEven` est une fonction prédicat qui vérifie si un nombre est pair. Nous utilisons ensuite `negate` pour créer une nouvelle fonction prédicat appelée `isOdd` qui vérifie si un nombre est impair en négant `isEven`. Enfin, nous utilisons `isOdd` avec la méthode `filter` pour filtrer les nombres pairs dans le tableau.
