# Fonction pour normaliser les sauts de ligne

Pour normaliser les sauts de ligne dans une chaîne de caractères, vous pouvez utiliser la fonction suivante.

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- Utilisez `String.prototype.replace()` avec une expression régulière pour correspondre et remplacer les sauts de ligne par la version `normalized`.
- Par défaut, la version `normalized` est définie sur `'\r\n'`.
- Pour utiliser une version `normalized` différente, passez-la en tant que deuxième argument.

Voici quelques exemples :

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
