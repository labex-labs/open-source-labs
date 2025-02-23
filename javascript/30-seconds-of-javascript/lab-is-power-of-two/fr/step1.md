# Vérifiez si un nombre est une puissance de deux

Pour vérifier si un nombre est une puissance de deux, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez l'opérateur binaire ET bit à bit (`&`) pour déterminer si le nombre (`n`) est une puissance de `2`.
3. De plus, vérifiez que `n` n'est pas faux.
4. Le code suivant vérifie fonctionnellement si `n` est une puissance de deux :

```js
const isPowerOfTwo = (n) => !!n && (n & (n - 1)) == 0;
```

Voici quelques exemples d'utilisation de la fonction `isPowerOfTwo` :

```js
isPowerOfTwo(0); // false
isPowerOfTwo(1); // true
isPowerOfTwo(8); // true
```
