# Complément logique

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Pour obtenir le complément logique d'une fonction `fn`, utilisez la fonction `complement`. Cette fonction renvoie une autre fonction qui applique l'opérateur logique non (`!`) sur le résultat de l'appel de `fn` avec tous les arguments fournis.

Voici un extrait de code d'exemple :

```js
const complement =
  (fn) =>
  (...args) =>
    !fn(...args);
```

Pour utiliser cette fonction, définissez une fonction prédicat, par exemple, `isEven` qui renvoie `true` si un nombre donné est pair. Vous pouvez ensuite obtenir le complément logique de cette fonction en utilisant la fonction `complement`, comme indiqué ci-dessous :

```js
const isEven = (num) => num % 2 === 0;
const isOdd = complement(isEven);
isOdd(2); // false
isOdd(3); // true
```
