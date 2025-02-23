# Voici comment arrondir un nombre à une précision donnée en JavaScript :

```
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`);
```

- Utilisez `Math.round()` et les littéraux de gabarit pour arrondir le nombre au nombre spécifié de chiffres.
- Si vous voulez arrondir à un entier, omettez le second argument, `decimals`.
- Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
- Par exemple, `round(1.005, 2)` renverra `1.01`.
