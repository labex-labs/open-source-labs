# Comment échapper les expressions régulières en JavaScript

Pour échapper une chaîne de caractères pour l'utiliser dans une expression régulière en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer le codage.
2. Utilisez `String.prototype.replace()` pour échapper les caractères spéciaux.
3. Copiez et collez le fragment de code suivant :

```js
const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
```

4. Utilisez la fonction `escapeRegExp()` pour échapper les caractères spéciaux dans une chaîne de caractères.

Voici un exemple :

```js
escapeRegExp("(test)"); // \\(test\\)
```

Avec ces étapes, vous pouvez désormais facilement échapper n'importe quel caractère spécial dans une expression régulière en JavaScript.
