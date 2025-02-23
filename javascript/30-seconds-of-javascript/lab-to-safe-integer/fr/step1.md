# Conversion d'une valeur en un entier sûr

Pour convertir une valeur en un entier sûr, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Math.max()` et `Math.min()` pour trouver la valeur sûre la plus proche.
3. Utilisez `Math.round()` pour convertir la valeur en un entier.

Voici un extrait de code d'exemple qui montre comment convertir une valeur en un entier sûr :

```js
const toSafeInteger = (num) =>
  Math.round(
    Math.max(Math.min(num, Number.MAX_SAFE_INTEGER), Number.MIN_SAFE_INTEGER)
  );
```

Vous pouvez tester cette fonction avec les entrées suivantes :

```js
toSafeInteger("3.2"); // 3
toSafeInteger(Infinity); // 9007199254740991
```
