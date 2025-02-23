# Trouver l'élément d'indice N d'un tableau

Pour trouver l'élément d'indice `n` d'un tableau, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.slice()` pour créer un nouveau tableau contenant l'élément d'indice `n`.
3. Si l'indice est en dehors des limites, renvoyez `undefined`.
4. Omettez le second argument, `n`, pour obtenir le premier élément du tableau.

Voici un exemple de code qui met en œuvre cela :

```js
const nthElement = (arr, n = 0) =>
  (n === -1 ? arr.slice(n) : arr.slice(n, n + 1))[0];
```

Vous pouvez tester cette fonction avec les exemples suivants :

```js
nthElement(["a", "b", "c"], 1); // Sortie : 'b'
nthElement(["a", "b", "b"], -3); // Sortie : 'a'
```

En suivant ces étapes, vous pouvez facilement trouver l'élément d'indice `n` d'un tableau à l'aide de JavaScript.
