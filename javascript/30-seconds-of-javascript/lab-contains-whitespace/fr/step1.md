# Vérification d'espaces blancs dans une chaîne

Pour vérifier si une chaîne contient des caractères d'espacement, suivez les étapes ci-dessous :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez `RegExp.prototype.test()` avec une expression régulière appropriée pour vérifier si la chaîne donnée contient des caractères d'espacement.
- Voici un extrait de code d'exemple :

  ```js
  const containsWhitespace = (str) => /\s/.test(str);
  ```

- Pour tester la fonction, appelez `containsWhitespace` avec une chaîne en tant qu'argument. Elle renverra `true` si la chaîne contient des caractères d'espacement, sinon `false`.

  ```js
  containsWhitespace("lorem"); // false
  containsWhitespace("lorem ipsum"); // true
  ```
