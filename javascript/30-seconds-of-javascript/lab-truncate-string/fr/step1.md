# Raccourcir une chaîne de caractères en JavaScript

Pour raccourcir une chaîne de caractères en JavaScript, vous pouvez utiliser la fonction `truncateString`. Cette fonction prend deux arguments : `str` (la chaîne de caractères à raccourcir) et `num` (la longueur maximale de la chaîne de caractères raccourcie).

La fonction `truncateString` vérifie si la longueur de `str` est supérieure à `num`. Si c'est le cas, la fonction raccourcit la chaîne de caractères à la longueur souhaitée et ajoute `'...'` à la fin. Sinon, elle renvoie la chaîne d'origine.

Voici le code de la fonction `truncateString` :

```js
const truncateString = (str, num) =>
  str.length > num ? str.slice(0, num > 3 ? num - 3 : num) + "..." : str;
```

Et voici un exemple d'utilisation de la fonction `truncateString` :

```js
truncateString("boomerang", 7); // 'boom...'
```
