# Fonction pour limiter un nombre à une plage

Pour limiter un nombre à une plage spécifiée, utilisez la fonction `clampNumber`.

Pour commencer, ouvrez le Terminal/SSH et tapez `node` pour pratiquer la programmation.

La fonction `clampNumber` prend trois paramètres : `num`, `a` et `b`. Elle limite `num` à l'intérieur de la plage inclusive spécifiée par les valeurs limites `a` et `b` et renvoie le résultat.

Si `num` est compris dans la plage, la fonction renvoie `num`. Sinon, elle renvoie le nombre le plus proche de la plage.

Voici le code de la fonction `clampNumber` :

```js
const clampNumber = (num, a, b) =>
  Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));
```

Et voici quelques exemples d'utilisation de la fonction :

```js
clampNumber(2, 3, 5); // 3
clampNumber(1, -1, -5); // -1
```
