# Comment calculer le logarithme dans une base spécifique

Pour calculer le logarithme d'un nombre donné dans une base spécifique, suivez ces étapes :

1. Ouvrez le Terminal ou SSH.
2. Tapez `node` pour commencer à pratiquer la programmation.
3. Utilisez le code suivant pour calculer le logarithme :

```js
const logBase = (n, base) => Math.log(n) / Math.log(base);
```

4. Remplacez `n` par le nombre donné et `base` par la base spécifique.
5. Exécutez le code pour obtenir le résultat.

Voici quelques exemples :

```js
logBase(10, 10); // 1
logBase(100, 10); // 2
```
