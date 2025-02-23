# Renverser un nombre

Pour renverser un nombre en utilisant JavaScript, vous pouvez utiliser la fonction `reverseNumber()` avec les étapes suivantes :

1. Convertissez le nombre `n` en chaîne de caractères à l'aide de `Object.prototype.toString()`.
2. Utilisez `String.prototype.split()`, `Array.prototype.reverse()` et `Array.prototype.join()` pour obtenir la valeur renversée de `n` sous forme de chaîne de caractères.
3. Convertissez la chaîne de caractères en nombre à l'aide de `parseFloat()`.
4. Conservez le signe du nombre à l'aide de `Math.sign()`.

Voici le code pour la fonction `reverseNumber()` :

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

Vous pouvez tester la fonction avec ces exemples :

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
