# Format Duration

Pour obtenir le format lisible par l'homme d'un nombre donné de millisecondes, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Divisez les `ms` par les valeurs appropriées pour obtenir les valeurs appropriées pour `jour`, `heure`, `minute`, `seconde` et `milliseconde`.
3. Utilisez `Object.entries()` avec `Array.prototype.filter()` pour ne conserver que les valeurs non nulles.
4. Créez la chaîne de caractères pour chaque valeur, en pluralisant approprié, en utilisant `Array.prototype.map()`.
5. Combinez les valeurs en une chaîne de caractères en utilisant `Array.prototype.join()`.

Voici le code :

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

Voici quelques exemples :

```js
formatDuration(1001); // '1 seconde, 1 milliseconde'
formatDuration(34325055574);
// '397 jours, 6 heures, 44 minutes, 15 secondes, 574 millisecondes'
```
