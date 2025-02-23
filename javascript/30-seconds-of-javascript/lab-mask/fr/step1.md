# Comment masquer une valeur en JavaScript

Pour masquer une valeur en JavaScript, vous pouvez utiliser la fonction `mask()`. Suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `String.prototype.slice()` pour extraire la partie des caractères qui restera non masquée.
3. Utilisez `String.prototype.padStart()` pour remplir le début de la chaîne avec le caractère de masquage jusqu'à la longueur d'origine.
4. Si vous voulez exclure des caractères de la fin de la chaîne, utilisez une valeur négative pour `num`.
5. Si vous ne spécifiez pas de valeur pour `num`, la fonction utilisera la valeur par défaut de 4 caractères non masqués.
6. Si vous ne spécifiez pas de valeur pour `mask`, la fonction utilisera le caractère `'*'` par défaut pour le masquage.

Voici le code de la fonction `mask()` :

```js
const mask = (cc, num = 4, mask = "*") =>
  `${cc}`.slice(-num).padStart(`${cc}`.length, mask);
```

Voici quelques exemples d'utilisation de la fonction `mask()` :

```js
mask(1234567890); // '******7890'
mask(1234567890, 3); // '*******890'
mask(1234567890, -4, "$"); // '$$$$567890'
```
