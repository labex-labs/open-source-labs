# Vérifier si une valeur est une fonction asynchrone en JavaScript

Pour vérifier si une valeur est une fonction `async` en JavaScript, vous pouvez utiliser le code suivant :

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

Cette fonction utilise `Object.prototype.toString()` et `Function.prototype.call()` pour vérifier si l'argument donné est une fonction `async`.

Vous pouvez tester la fonction en passant une fonction normale et une fonction `async` en tant qu'arguments :

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

Pour commencer à pratiquer la programmation en JavaScript, ouvrez le Terminal/SSH et tapez `node`.
