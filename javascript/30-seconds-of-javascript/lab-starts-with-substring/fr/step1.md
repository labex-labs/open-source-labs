# Fonction pour vérifier si une chaîne de caractères commence par une sous-chaîne

Pour vérifier si une chaîne de caractères donnée commence par une sous-chaîne d'une autre chaîne de caractères, suivez les étapes ci-dessous :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez une boucle `for...in` et la méthode `String.prototype.slice()` pour obtenir chaque sous-chaîne du mot donné, en commençant par le début.
- Utilisez la méthode `String.prototype.startsWith()` pour vérifier la sous-chaîne actuelle par rapport au `text`.
- Si une sous-chaîne correspondante est trouvée, renvoyez-la. Sinon, renvoyez `undefined`.

Voici une fonction JavaScript qui le fait :

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

Vous pouvez appeler cette fonction comme suit :

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // renvoie '/>'
```
