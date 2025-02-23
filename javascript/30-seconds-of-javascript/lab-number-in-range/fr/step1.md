# Fonction pour vérifier si un nombre est dans une plage donnée

Pour vérifier si un nombre se situe dans une plage spécifiée, utilisez la fonction `inRange`. Commencez par ouvrir le Terminal/SSH et taper `node` pour commencer à coder.

Voici les étapes pour utiliser la fonction `inRange` :

1. Utilisez une comparaison arithmétique pour vérifier si le nombre donné est dans la plage spécifiée.
2. Si le deuxième argument, `end`, n'est pas spécifié, la plage est considérée comme allant de `0` à `start`.
3. La fonction `inRange` prend trois arguments : `n`, `start` et `end`.
4. Si `end` est inférieur à `start`, la fonction échange les valeurs de `start` et `end`.
5. Si `end` n'est pas spécifié, la fonction vérifie si `n` est supérieur ou égal à 0 et inférieur à `start`.
6. Si `end` est spécifié, la fonction vérifie si `n` est supérieur ou égal à `start` et inférieur à `end`.
7. La fonction renvoie `true` si `n` est dans la plage spécifiée, et `false` sinon.

Voici la fonction `inRange` :

```js
const inRange = (n, start, end = null) => {
  if (end && start > end) [end, start] = [start, end];
  return end == null ? n >= 0 && n < start : n >= start && n < end;
};
```

Voici quelques exemples d'utilisation de la fonction `inRange` :

```js
inRange(3, 2, 5); // true
inRange(3, 4); // true
inRange(2, 3, 5); // false
inRange(3, 2); // false
```
