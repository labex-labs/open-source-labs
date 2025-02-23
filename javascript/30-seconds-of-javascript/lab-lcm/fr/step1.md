# Calculer le plus petit commun multiple

Pour calculer le plus petit commun multiple de deux ou plusieurs nombres, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la formule du plus grand commun diviseur (PGCD) et le fait que `ppcm(x, y) = x * y / pgcd(x, y)` pour déterminer le plus petit commun multiple.
3. La formule du PGCD utilise la récursion.
4. Implémentez le code suivant en JavaScript :

```js
const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y));
  const _lcm = (x, y) => (x * y) / gcd(x, y);
  return [...arr].reduce((a, b) => _lcm(a, b));
};
```

Utilisation exemple :

```js
lcm(12, 7); // 84
lcm(...[1, 3, 4, 5]); // 60
```
