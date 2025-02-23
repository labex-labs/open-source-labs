# Fonction pour remplir une chaîne de caractères

Pour remplir une chaîne de caractères de chaque côté avec le caractère spécifié, si elle est plus courte que la `length` spécifiée, utilisez la fonction suivante :

```js
const pad = (str, length, char = " ") =>
  str.padStart((str.length + length) / 2, char).padEnd(length, char);
```

La fonction utilise `String.prototype.padStart()` et `String.prototype.padEnd()` pour remplir les deux côtés de la chaîne de caractères donnée. Vous pouvez omettre le troisième argument, `char`, pour utiliser le caractère d'espacement comme caractère de remplissage par défaut.

Voici quelques exemples d'utilisation de la fonction `pad()` :

```js
pad("cat", 8); // '  cat   '
pad(String(42), 6, "0"); // '004200'
pad("foobar", 3); // 'foobar'
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
