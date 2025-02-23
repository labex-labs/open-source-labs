# Code Practice: Left Substring Generator

Pour générer toutes les sous-chaînes gauches d'une chaîne de caractères donnée, utilisez la fonction `leftSubstrGenerator` fournie ci-dessous.

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

Pour utiliser la fonction, ouvrez le Terminal/SSH et tapez `node`. Ensuite, entrez la fonction avec un argument de chaîne de caractères :

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

La fonction utilise `String.prototype.length` pour terminer rapidement si la chaîne est vide et une boucle `for...in` avec `String.prototype.slice()` pour `produire` chaque sous-chaîne de la chaîne donnée, en commençant par le début.
