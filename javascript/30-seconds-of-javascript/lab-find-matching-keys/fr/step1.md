# Trouver les clés correspondantes

Pour trouver toutes les clés dans un objet qui correspondent à une valeur donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.keys()` pour obtenir toutes les propriétés de l'objet.
3. Utilisez `Array.prototype.filter()` pour tester chaque paire clé-valeur et renvoyer toutes les clés qui sont égales à la valeur donnée.

Voici une fonction d'exemple qui implémente cette logique :

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

Vous pouvez utiliser cette fonction comme suit :

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
