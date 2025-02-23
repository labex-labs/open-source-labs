# Comment calculer le plus grand diviseur commun

Pour calculer le plus grand diviseur commun entre deux ou plusieurs nombres / tableaux en utilisant du code, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez le code suivant :

```js
const gcd = (...arr) => {
  const _gcd = (x, y) => (!y ? x : gcd(y, x % y));
  return [...arr].reduce((a, b) => _gcd(a, b));
};
```

3. La fonction `gcd` utilise la récursion.

4. Le cas de base est lorsque `y` est égal à `0`. Dans ce cas, la fonction renvoie `x`.

5. Sinon, la fonction renvoie le PPCM de `y` et du reste de la division `x / y`.

6. Pour tester la fonction, utilisez le code suivant :

```js
gcd(8, 36); // 4
gcd(...[12, 8, 32]); // 4
```
