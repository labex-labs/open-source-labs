# Conversion de nombres en notation à virgule fixe

Pour convertir un nombre en notation à virgule fixe sans zéros de fin, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Number.prototype.toFixed()` pour convertir le nombre en une chaîne de caractères en notation à virgule fixe.
3. Utilisez `Number.parseFloat()` pour convertir la chaîne de caractères en notation à virgule fixe en retournant un nombre, en supprimant les zéros de fin.
4. Utilisez une littérale de gabarit pour convertir le nombre en une chaîne de caractères.

Exemple de code :

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

Vous pouvez tester la fonction avec différents entrées :

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.5, 2); // '1.5'
```
