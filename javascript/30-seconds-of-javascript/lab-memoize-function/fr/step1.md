# Mémoïsation d'une fonction

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`. Cette fonction renvoie la fonction mémoïsée (mise en cache). Voici les étapes pour utiliser cette fonction :

1. Instanciez un nouvel objet `Map` pour créer un cache vide.
2. Retournez une fonction qui prend un seul argument qui sera fourni à la fonction mémoïsée. Avant d'exécuter la fonction, vérifiez si la sortie pour cette valeur d'entrée spécifique est déjà mise en cache. Si c'est le cas, renvoyez la sortie mise en cache ; sinon, stockez-la et renvoyez-la.
3. Utilisez le mot clé `function` pour permettre à la fonction mémoïsée d'avoir son contexte `this` modifié si nécessaire.
4. Définissez le `cache` comme propriété sur la fonction renvoyée pour permettre d'y accéder.

Voici le code qui implémente la fonction de mémoïsation :

```js
const memoize = (fn) => {
  const cache = new Map();
  const cached = function (val) {
    return cache.has(val)
      ? cache.get(val)
      : cache.set(val, fn.call(this, val)) && cache.get(val);
  };
  cached.cache = cache;
  return cached;
};
```

Pour voir comment cette fonction fonctionne, vous pouvez l'utiliser avec la fonction `anagrams`. Voici un exemple :

```js
const anagramsCached = memoize(anagrams);
anagramsCached("javascript"); // prend beaucoup de temps
anagramsCached("javascript"); // renvoie pratiquement instantanément car c'est mis en cache
console.log(anagramsCached.cache); // La carte d'anagrammes mise en cache
```
