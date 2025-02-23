# Vérifier si une valeur est une fonction génératrice

Pour vérifier si une valeur est une fonction génératrice, vous pouvez utiliser la fonction `isGeneratorFunction`. Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici comment fonctionne la fonction `isGeneratorFunction` :

- Elle vérifie si l'argument donné est une fonction génératrice en utilisant `Object.prototype.toString()` et `Function.prototype.call()`.
- Si le résultat du contrôle est `'[object GeneratorFunction]'`, alors la valeur est une fonction génératrice.

Voici le code de la fonction `isGeneratorFunction` :

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

Et voici quelques exemples d'utilisation :

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
