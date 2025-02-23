# Explanation of Juxtapose Functions

Pour utiliser la fonction `juxt`, ouvrez d'abord le Terminal/SSH et tapez `node` pour commencer à pratiquer le codage. La fonction `juxt` prend plusieurs fonctions en arguments et renvoie une fonction qui est la juxtaposition de ces fonctions.

Pour créer la fonction `juxt`, utilisez `Array.prototype.map()` pour renvoyer une `fn` qui peut prendre un nombre variable d'`args`. Lorsque `fn` est appelée, elle devrait renvoyer un tableau contenant le résultat de l'application de chaque `fn` aux `args`.

Voici une implémentation exemple de la fonction `juxt`:

```js
const juxt =
  (...fns) =>
  (...args) =>
    [...fns].map((fn) => [...args].map(fn));
```

Une fois que vous avez défini la fonction `juxt`, vous pouvez l'utiliser en passant un nombre quelconque de fonctions en arguments, suivies d'un nombre quelconque d'arguments à passer à ces fonctions.

Voici quelques exemples d'utilisation de la fonction `juxt`:

```js
juxt(
  (x) => x + 1,
  (x) => x - 1,
  (x) => x * 10
)(1, 2, 3); // [[2, 3, 4], [0, 1, 2], [10, 20, 30]]
```

```js
juxt(
  (s) => s.length,
  (s) => s.split(" ").join("-")
)("happy coding"); // [[18], ['happy-coding']]
```

Dans le premier exemple, la fonction `juxt` prend trois fonctions en arguments et renvoie une nouvelle fonction. Lorsque cette nouvelle fonction est appelée avec les arguments `1, 2, 3`, elle applique chacune des trois fonctions à ces arguments et renvoie un tableau de tableaux contenant les résultats.

Dans le second exemple, la fonction `juxt` prend deux fonctions en arguments et renvoie une nouvelle fonction. Lorsque cette nouvelle fonction est appelée avec l'argument `'happy-coding'`, elle applique chacune des deux fonctions à cet argument et renvoie un tableau de tableaux contenant les résultats.
