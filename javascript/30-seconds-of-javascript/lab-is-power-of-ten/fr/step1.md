# Vérifiez si un nombre est une puissance de dix

Pour vérifier si un nombre est une puissance de dix, ouvrez le Terminal/SSH et tapez `node`.

Voici le code que vous pouvez utiliser pour déterminer si `n` est une puissance de `10` :

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

Utilisez la fonction `isPowerOfTen()` pour déterminer si un nombre donné est une puissance de dix.

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
