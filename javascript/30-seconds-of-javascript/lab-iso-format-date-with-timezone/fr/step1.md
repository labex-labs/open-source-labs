# Conversion de dates au format ISO avec fuseau horaire

Pour convertir une date au format ISO étendu (ISO 8601), y compris le décalage horaire, suivez ces étapes :

1. Ouvrez le Terminal/SSH et entrez `node` pour commencer à coder.
2. Utilisez `Date.prototype.getTimezoneOffset()` pour obtenir le décalage horaire et le inverser. Stockez son signe dans `diff`.
3. Définissez une fonction d'aide, `pad()`, qui normalise tout nombre passé en un entier en utilisant `Math.floor()` et `Math.abs()` et le complète à `2` chiffres, en utilisant `String.prototype.padStart()`.
4. Utilisez `pad()` et les méthodes intégrées dans le prototype `Date` pour construire la chaîne ISO 8601 avec décalage horaire.

Voici le code que vous pouvez utiliser :

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

Utilisez la fonction `toISOStringWithTimezone()` avec un objet `new Date()` en tant qu'argument pour obtenir la date au format ISO avec décalage horaire. Par exemple :

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
