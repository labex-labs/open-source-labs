# Comment trouver l'élément le plus long dans un tableau

Pour trouver l'élément le plus long dans un tableau, ouvrez le Terminal/SSH et tapez `node`. La fonction prend un nombre quelconque d'objets itérables ou d'objets possédant une propriété `length` et renvoie celui qui est le plus long. Elle utilise `Array.prototype.reduce()` pour comparer la longueur des objets et trouver celui qui est le plus long. Si plusieurs objets ont la même longueur, la fonction renvoie le premier. Si aucun argument n'est fourni, elle renvoie `undefined`.

Voici le code :

```js
const longestItem = (...vals) =>
  vals.reduce((a, x) => (x.length > a.length ? x : a));
```

Vous pouvez utiliser la fonction de la manière suivante :

```js
longestItem("this", "is", "a", "testcase"); // 'testcase'
longestItem(...["a", "ab", "abc"]); // 'abc'
longestItem(...["a", "ab", "abc"], "abcd"); // 'abcd'
longestItem([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]); // [1, 2, 3, 4, 5]
longestItem([1, 2, 3], "foobar"); // 'foobar'
```
