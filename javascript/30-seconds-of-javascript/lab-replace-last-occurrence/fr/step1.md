# Fonction pour remplacer la dernière occurrence d'un motif dans une chaîne de caractères

Voici une fonction qui remplace la dernière occurrence d'un motif dans une chaîne de caractères :

```js
const replaceLast = (str, pattern, replacement) => {
```

Pour l'utiliser, ouvrez le Terminal/SSH et tapez `node`.

- Tout d'abord, utilisez `typeof` pour déterminer si `pattern` est une chaîne de caractères ou une expression régulière.
- Si le `pattern` est une chaîne de caractères, utilisez - le comme `match`.
- Sinon, utilisez le constructeur `RegExp` pour créer une nouvelle expression régulière en utilisant la propriété `RegExp.prototype.source` du `pattern` et en lui ajoutant le marqueur `'g'`. Utilisez `String.prototype.match()` et `Array.prototype.slice()` pour obtenir le dernier match, s'il y en a un.

```js
const match =
  typeof pattern === "string"
    ? pattern
    : (str.match(new RegExp(pattern.source, "g")) || []).slice(-1)[0];
```

- Utilisez `String.prototype.lastIndexOf()` pour trouver la dernière occurrence du match dans la chaîne de caractères.
- Si un match est trouvé, utilisez `String.prototype.slice()` et une chaîne de caractères modèle (template literal) pour remplacer la sous - chaîne correspondante par le `replacement` donné.
- Si aucun match n'est trouvé, retournez la chaîne de caractères originale.

```js
  if (!match) return str;
  const last = str.lastIndexOf(match);
  return last!== -1
   ? `${str.slice(0, last)}${replacement}${str.slice(last + match.length)}`
    : str;
};
```

Voici quelques exemples d'utilisation de la fonction :

```js
replaceLast("abcabdef", "ab", "gg"); // 'abcggdef'
replaceLast("abcabdef", /ab/, "gg"); // 'abcggdef'
replaceLast("abcabdef", "ad", "gg"); // 'abcabdef'
replaceLast("abcabdef", /ad/, "gg"); // 'abcabdef'
```
