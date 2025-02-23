# Une fonction qui obtient le n-ième argument

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Voici comment vous pouvez créer une fonction qui obtient l'argument à l'index `n`.

- Utilisez `Array.prototype.slice()` pour obtenir l'argument souhaité à l'index `n`.
- Si `n` est négatif, l'argument n-ième à partir de la fin est renvoyé.

```js
const nthArg =
  (n) =>
  (...args) =>
    args.slice(n)[0];
```

Voici un exemple de manière d'utiliser la fonction `nthArg` :

```js
const third = nthArg(2);
console.log(third(1, 2, 3)); // Sortie : 3
console.log(third(1, 2)); // Sortie : undefined

const last = nthArg(-1);
console.log(last(1, 2, 3, 4, 5)); // Sortie : 5
```
