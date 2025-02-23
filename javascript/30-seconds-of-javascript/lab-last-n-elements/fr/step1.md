# Comment obtenir les derniers n éléments d'un tableau en JavaScript

Pour obtenir les derniers `n` éléments d'un tableau en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez `Array.prototype.slice()` avec une valeur de départ de `-n` pour obtenir les derniers `n` éléments du tableau.

Voici le code JavaScript pour obtenir les derniers `n` éléments d'un tableau :

```js
const lastN = (arr, n) => arr.slice(-n);
```

Pour tester le code, appelez la fonction `lastN()` avec le tableau et le nombre d'éléments que vous voulez obtenir, comme ceci :

```js
lastN(["a", "b", "c", "d"], 2); // ['c', 'd']
```
