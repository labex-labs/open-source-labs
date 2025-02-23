# Code Practice: Quotient et Module de la Division

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Ce code renvoie un tableau qui contient le quotient et le reste des nombres donnés.

Pour obtenir le quotient de la division `x / y`, utilisez `Math.floor()`. Pour obtenir le reste de la division `x / y`, utilisez l'opérateur modulo (`%`).

```js
const divmod = (x, y) => [Math.floor(x / y), x % y];
```

Par exemple :

```js
divmod(8, 3); // [2, 2]
divmod(3, 8); // [0, 3]
divmod(5, 5); // [1, 0]
```
