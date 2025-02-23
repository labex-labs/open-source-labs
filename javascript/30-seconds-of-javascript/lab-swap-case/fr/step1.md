# Comment inverser la casse d'une chaîne de caractères en JavaScript

Pour inverser la casse d'une chaîne de caractères en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez l'opérateur de propagation (`...`) pour convertir la chaîne d'entrée `str` en un tableau de caractères.
3. Utilisez `String.prototype.toLowerCase()` et `String.prototype.toUpperCase()` pour convertir les caractères en minuscules en majuscules et vice versa.
4. Utilisez `Array.prototype.map()` pour appliquer la transformation à chaque caractère, et `Array.prototype.join()` pour recombiner les caractères en une chaîne de caractères.
5. Notez que inverser la casse d'une chaîne de caractères deux fois ne résultera pas nécessairement dans la chaîne d'origine.

Voici un extrait de code d'exemple qui montre comment inverser la casse d'une chaîne de caractères en JavaScript :

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // Sortie : 'hELLO WORLD!'
```
