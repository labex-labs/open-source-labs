# Calcul du coefficient binomial

Pour calculer le nombre de manières de choisir `k` éléments parmi `n` éléments sans répétition et sans ordre, vous pouvez utiliser la fonction JavaScript suivante :

```js
const binomialCoefficient = (n, k) => {
  if (Number.isNaN(n) || Number.isNaN(k)) return NaN;
  if (k < 0 || k > n) return 0;
  if (k === 0 || k === n) return 1;
  if (k === 1 || k === n - 1) return n;
  if (n - k < k) k = n - k;
  let res = n;
  for (let j = 2; j <= k; j++) res *= (n - j + 1) / j;
  return Math.round(res);
};
```

Pour utiliser la fonction, ouvrez le Terminal/SSH et tapez `node`. Ensuite, appelez la fonction avec les valeurs souhaitées. Par exemple :

```js
binomialCoefficient(8, 2); // 28
```

Pour vous assurer que la fonction fonctionne correctement, vous pouvez suivre ces étapes :

1. Utilisez `Number.isNaN()` pour vérifier si l'une des deux valeurs est `NaN`.
2. Vérifiez si `k` est inférieur à `0`, supérieur ou égal à `n`, égal à `1` ou `n - 1` et renvoyez le résultat approprié.
3. Vérifiez si `n - k` est inférieur à `k` et inversez leurs valeurs en conséquence.
4. Bouclez de `2` à `k` et calculez le coefficient binomial.
5. Utilisez `Math.round()` pour prendre en compte les erreurs d'arrondi dans le calcul.
