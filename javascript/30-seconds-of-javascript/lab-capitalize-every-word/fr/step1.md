# Comment mettre en majuscule chaque mot en JavaScript

Pour mettre en majuscule chaque mot dans une chaîne de caractères à l'aide de JavaScript, vous pouvez utiliser la méthode `String.prototype.replace()` pour correspondre au premier caractère de chaque mot, puis utiliser la méthode `String.prototype.toUpperCase()` pour le mettre en majuscule.

Voici un extrait de code exemple que vous pouvez utiliser :

```js
const capitalizeEveryWord = (str) =>
  str.replace(/\b[a-z]/g, (char) => char.toUpperCase());
```

Pour utiliser cette fonction, passez la chaîne de caractères que vous voulez mettre en majuscule en tant qu'argument, comme ceci :

```js
capitalizeEveryWord("hello world!"); // 'Hello World!'
```

Cela retournera la chaîne de caractères mise en majuscule 'Hello World!'.
