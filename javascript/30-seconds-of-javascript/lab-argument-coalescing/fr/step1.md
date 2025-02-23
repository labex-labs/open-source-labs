# Utilisation de la coalescence d'arguments

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`. La coalescence d'arguments est une technique utilisée pour renvoyer le premier argument défini et non nul dans une liste d'arguments. Pour y arriver, utilisez `Array.prototype.find()` et `Array.prototype.includes()` pour trouver la première valeur qui n'est pas égale à `undefined` ou `null`.

Voici un exemple d'utilisation de la coalescence d'arguments en JavaScript :

```js
const coalesce = (...args) => args.find((v) => ![undefined, null].includes(v));
```

Dans le extrait de code ci-dessus, `coalesce` est une fonction qui prend un nombre quelconque d'arguments et renvoie le premier argument défini et non nul. Voici un exemple d'utilisation de la fonction `coalesce` :

```js
coalesce(null, undefined, "", NaN, "Waldo"); // ''
```

Dans cet exemple, `coalesce` est appelée avec une liste d'arguments qui inclut `null`, `undefined`, une chaîne de caractères vide `''`, `NaN` et la chaîne de caractères `'Waldo'`. La fonction renvoie une chaîne de caractères vide `''` car c'est le premier argument défini et non nul de la liste.
