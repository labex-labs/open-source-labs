# Comment vérifier si une date est valide

Pour vérifier si une date est valide, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez l'opérateur de propagation (`...`) pour passer le tableau d'arguments au constructeur `Date`.
3. Utilisez `Date.prototype.valueOf()` et `Number.isNaN()` pour vérifier si un objet `Date` valide peut être créé à partir des valeurs données.

Voici un extrait de code d'exemple :

```js
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());
```

Vous pouvez tester la fonction avec différentes valeurs, comme indiqué ci-dessous :

```js
isDateValid("December 17, 1995 03:24:00"); // true
isDateValid("1995-12-17T03:24:00"); // true
isDateValid("1995-12-17 T03:24:00"); // false
isDateValid("Duck"); // false
isDateValid(1995, 11, 17); // true
isDateValid(1995, 11, 17, "Duck"); // false
isDateValid({}); // false
```
