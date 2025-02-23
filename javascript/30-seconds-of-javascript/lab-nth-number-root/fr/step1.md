# Comment calculer la racine n-ième d'un nombre

Pour calculer la racine n-ième d'un nombre :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la formule `Math.pow(x, 1/n)` pour calculer `x` à la puissance `1/n`.
3. Le résultat de ce calcul est égal à la racine n-ième de `x`.

Voici un extrait de code d'exemple :

```js
const nthRoot = (x, n) => Math.pow(x, 1 / n);
nthRoot(32, 5); // Sortie : 2
```

Ce code calculera la racine n-ième de 32 (où n est 5) et renverra la sortie sous forme de 2.
