# Fonction pour Trouver la Première Clé Correspondant à un Test

Pour trouver la première clé dans un objet qui correspond à une fonction de test donnée, utilisez la fonction `findKey()`. Tout d'abord, obtenez toutes les propriétés de l'objet en utilisant `Object.keys()`. Ensuite, appliquez la fonction de test à chaque paire clé-valeur en utilisant `Array.prototype.find()`. La fonction de test devrait prendre trois arguments : la valeur, la clé et l'objet. La fonction renvoie la première clé qui satisfait la fonction de test ou `undefined` si aucune n'est trouvée.

Voici une implémentation de `findKey()` :

```js
const findKey = (obj, fn) =>
  Object.keys(obj).find((key) => fn(obj[key], key, obj));
```

Pour utiliser `findKey()`, passez l'objet et la fonction de test en arguments :

```js
findKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'barney'
```

Dans cet exemple, `findKey()` renvoie la première clé dans l'objet où la valeur de la propriété `active` est `true`, qui est `'barney'`.
