# Sous-tableaux d'éléments consécutifs

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Le code suivant crée un tableau d' n-uplets d'éléments consécutifs.

```js
const aperture = (n, arr) =>
  n > arr.length ? [] : arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

Pour utiliser la fonction :

- Appelez la fonction `aperture(n, arr)` avec `n` comme nombre d'éléments consécutifs et `arr` comme tableau de nombres.
- La fonction renvoie un tableau d' n-uplets d'éléments consécutifs de `arr`.
- Si `n` est supérieur à la longueur de `arr`, la fonction renvoie un tableau vide.

Utilisation exemple :

```js
aperture(2, [1, 2, 3, 4]); // [[1, 2], [2, 3], [3, 4]]
aperture(3, [1, 2, 3, 4]); // [[1, 2, 3], [2, 3, 4]]
aperture(5, [1, 2, 3, 4]); // []
```
