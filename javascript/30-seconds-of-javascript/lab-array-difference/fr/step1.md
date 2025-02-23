# Différence entre deux tableaux

Pour trouver la différence entre deux tableaux, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.

2. Créez un `Set` à partir du tableau `b` pour extraire les valeurs uniques de `b`.

3. Utilisez `Array.prototype.filter()` sur le tableau `a` pour ne conserver que les valeurs qui ne sont pas dans le tableau `b`, en utilisant `Set.prototype.has()`.

Voici le code :

```js
const difference = (a, b) => {
  const s = new Set(b);
  return a.filter((x) => !s.has(x));
};
```

Utilisation de l'exemple :

```js
difference([1, 2, 3, 3], [1, 2, 4]); // Sortie : [3, 3]
```
