# Exécution de promesses en série

Pour exécuter une série de promesses, utilisez `Array.prototype.reduce()` pour créer une chaîne de promesses. Chaque promesse renvoie la prochaine promesse après avoir été résolue.

Pour commencer, ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

Voici un exemple de code :

```js
const runPromisesInSeries = (ps) =>
  ps.reduce((p, next) => p.then(next), Promise.resolve());
```

Vous pouvez ensuite utiliser la fonction `runPromisesInSeries` pour exécuter séquentiellement des promesses, comme dans l'exemple suivant :

```js
const delay = (d) => new Promise((r) => setTimeout(r, d));
runPromisesInSeries([() => delay(1000), () => delay(2000)]);
// Ce code exécute chaque promesse séquentiellement, prenant au total 3 secondes pour se terminer.
```
