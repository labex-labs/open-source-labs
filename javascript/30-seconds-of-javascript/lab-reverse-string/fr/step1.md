# Voici une fonction pour inverser une chaîne de caractères :

Pour inverser une chaîne de caractères, utilisez l'opérateur de propagation (`...`) et `Array.prototype.reverse()`. Combinez les caractères pour obtenir une chaîne de caractères en utilisant `Array.prototype.join()`. Voici le code :

```js
const reverseString = (str) => [...str].reverse().join("");
```

Utilisation de l'exemple :

```js
reverseString("foobar"); // 'raboof'
```
