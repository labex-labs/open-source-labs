# Conversion d'une fonction variadique

Pour convertir une fonction variadique, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.
2. Créez une fonction qui prend une fonction variadique.
3. Utilisez une fermeture et l'opérateur de propagation (`...`) pour mapper le tableau d'arguments aux entrées de la fonction.
4. Retournez une nouvelle fonction qui accepte un tableau d'arguments et appelle la fonction variadique d'origine avec ces arguments.

Voici un exemple de la manière d'utiliser cette technique pour convertir la fonction `Math.max` :

```js
const spreadOver = (fn) => (argsArr) => fn(...argsArr);

const arrayMax = spreadOver(Math.max);
arrayMax([1, 2, 3]); // 3
```
