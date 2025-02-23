# Une fonction pour vérifier si une chaîne se termine par une sous-chaîne

Pour vérifier si une chaîne de caractères donnée se termine par une sous-chaîne d'une autre chaîne, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez une boucle `for...in` et `String.prototype.slice()` pour obtenir chaque sous-chaîne de la chaîne `word` donnée, en commençant par la fin.
3. Utilisez `String.prototype.endsWith()` pour vérifier la sous-chaîne actuelle par rapport au `text`.
4. Retournez la sous-chaîne correspondante, si elle est trouvée. Sinon, retournez `undefined`.

Voici le extrait de code pour implémenter les étapes ci-dessus :

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

Vous pouvez tester la fonction avec l'exemple suivant :

```js
endsWithSubstring("Lorem ipsum dolor sit amet<br /", "<br />"); // '<br /'
```
