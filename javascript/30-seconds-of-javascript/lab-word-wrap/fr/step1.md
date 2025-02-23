# Instructions pour envelopper une chaîne de caractères

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Ce code enveloppe une chaîne de caractères à un nombre donné de caractères en utilisant un caractère de rupture de chaîne. Pour l'utiliser, suivez ces étapes :

1. Utilisez `String.prototype.replace()` et une expression régulière pour insérer un caractère de rupture donné au plus proche espace blanc de `max` caractères.
2. Si vous ne voulez pas utiliser la valeur par défaut de `'\n'` pour le troisième argument, `br`, vous pouvez l'omettre et fournir votre propre caractère.

Voici le code :

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

Et voici quelques exemples d'utilisation :

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
