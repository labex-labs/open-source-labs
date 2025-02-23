# Pluralize String

Pour pluraliser un mot en fonction d'un nombre donné, utilisez la fonction `pluralize`. Commencez par ouvrir le Terminal/SSH et tapez `node`. Cette fonction peut renvoyer soit la forme singulière soit la forme plurielle du mot, selon le nombre d'entrée. Vous pouvez également fournir un dictionnaire optionnel pour utiliser des formes plurelles personnalisées.

Pour définir la fonction `pluralize`, utilisez une fermeture qui prend le `mot` et une forme `plurielle` optionnelle. Si l'entrée `num` est soit `-1` soit `1`, renvoyez la forme singulière du `mot`. Sinon, renvoyez la forme `plurielle`. Si aucune forme `plurielle` personnalisée n'est fournie, la fonction utilisera la valeur par défaut du mot singulier + `s`.

Si le premier argument est un objet, la fonction `pluralize` renvoie une nouvelle fonction qui peut utiliser le dictionnaire fourni pour résoudre la forme plurielle correcte du `mot`.

Voici la fonction `pluralize` en action :

```js
const pluralize = (val, word, plural = word + "s") => {
  const _pluralize = (num, word, plural = word + "s") =>
    [1, -1].includes(Number(num)) ? word : plural;
  if (typeof val === "object")
    return (num, word) => _pluralize(num, word, val[word]);
  return _pluralize(val, word, plural);
};
```

Vous pouvez utiliser la fonction `pluralize` comme ceci :

```js
pluralize(0, "apple"); // 'apples'
pluralize(1, "apple"); // 'apple'
pluralize(2, "apple"); // 'apples'
pluralize(2, "person", "people"); // 'people'
```

Si vous avez un dictionnaire de formes plurelles personnalisées, vous pouvez créer une fonction `autoPluralize` qui utilise automatiquement la forme plurielle correcte pour un `mot` donné :

```js
const PLURALS = {
  person: "people",
  radius: "radii"
};
const autoPluralize = pluralize(PLURALS);
autoPluralize(2, "person"); // 'people'
```
