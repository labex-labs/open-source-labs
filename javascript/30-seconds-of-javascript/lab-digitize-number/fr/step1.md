# Comment numériser un nombre

Pour numériser un nombre en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Math.abs()` pour supprimer le signe du nombre.
3. Convertissez le nombre en chaîne de caractères et utilisez l'opérateur de répandage (`...`) pour créer un tableau de chiffres.
4. Utilisez `Array.prototype.map()` et `parseInt()` pour convertir chaque chiffre en un entier.

Voici le code pour la fonction `digitize` :

```js
const digitize = (n) => [...`${Math.abs(n)}`].map((i) => parseInt(i));
```

Utilisation de l'exemple :

```js
digitize(123); // [1, 2, 3]
digitize(-123); // [1, 2, 3]
```
