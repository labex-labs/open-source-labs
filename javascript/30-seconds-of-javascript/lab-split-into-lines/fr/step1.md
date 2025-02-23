# Comment commencer à pratiquer la programmation dans le Terminal/SSH

Pour commencer à pratiquer la programmation dans le Terminal/SSH, il suffit de taper `node`.

# Diviser une chaîne de caractères multiligne en un tableau de lignes

Pour diviser une chaîne de caractères multiligne en un tableau de lignes :

- Utilisez `String.prototype.split()` et une expression régulière pour correspondre aux sauts de ligne et créer un tableau.
- L'expression régulière `/\r?\n/` correspond à tous les sauts de ligne `\r` et `\n`.
- Cela renverra un tableau de lignes.

```js
const splitLines = (str) => str.split(/\r?\n/);
```

```js
splitLines("This\nis a\nmultiline\nstring.\n");
// ['This', 'is a','multiline','string.', '']
```
