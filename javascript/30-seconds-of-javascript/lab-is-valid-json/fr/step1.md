# Vérifier si une chaîne est un JSON valide

Pour vérifier si une chaîne donnée est un JSON valide, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `JSON.parse()` et un bloc `try...catch` pour vérifier si la chaîne fournie est un JSON valide.
3. Si la chaîne est valide, renvoyez `true`. Sinon, renvoyez `false`.

Voici un extrait de code d'exemple qui implémente cette logique :

```js
const isValidJSON = (str) => {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
};
```

Vous pouvez tester cette fonction avec différentes chaînes d'entrée, comme ceci :

```js
isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // false
```

Dans le dernier exemple, `null` n'est pas une chaîne JSON valide, donc la fonction renvoie `false`.
