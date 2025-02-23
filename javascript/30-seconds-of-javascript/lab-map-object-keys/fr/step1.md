# Fonction pour mapper les clés d'un objet

Pour mapper les clés d'un objet à l'aide d'une fonction fournie et générer un nouvel objet, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.keys()` pour itérer sur les clés de l'objet.
3. Utilisez `Array.prototype.reduce()` pour créer un nouvel objet avec les mêmes valeurs et les clés mappées à l'aide de la fonction fournie (`fn`).

Voici une implémentation de l'exemple de la fonction `mapKeys` :

```js
const mapKeys = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[fn(obj[k], k, obj)] = obj[k];
    return acc;
  }, {});
```

Vous pouvez tester la fonction avec une entrée d'exemple comme ceci :

```js
mapKeys({ a: 1, b: 2 }, (val, key) => key + val); // { a1: 1, b2: 2 }
```
