# Générateur de sous-chaînes droites

Pour générer toutes les sous-chaînes droites d'une chaîne donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `String.prototype.length` pour arrêter l'itération tôt si la chaîne est vide.
3. Utilisez une boucle `for...in` et `String.prototype.slice()` pour `produire` chaque sous-chaîne de la chaîne donnée, en commençant par la fin.

Voici le bout de code :

```js
const rightSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(-i - 1);
};
```

Utilisation exemple :

```js
[...rightSubstrGenerator("hello")];
// [ 'o', 'lo', 'llo', 'ello', 'hello' ]
```
