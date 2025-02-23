# Code de la fabrique de coalescence d'arguments

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`. Cette fonction renvoie le premier argument qui évalue à `true` sur la base du validateur passé en argument.

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

Utilisez `Array.prototype.find()` pour renvoyer le premier argument qui renvoie `true` à partir de la fonction de validation d'arguments fournie, `valid`. Par exemple,

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

Ici, la fonction `coalesceFactory` est personnalisée pour créer la fonction `customCoalesce`. La fonction `customCoalesce` filtre `null`, `undefined`, `NaN` et les chaînes de caractères vides des arguments fournis et renvoie le premier argument qui n'est pas filtré. La sortie de `customCoalesce(undefined, null, NaN, '', 'Waldo')` est `'Waldo'`.
