# Fonction pour mapper les valeurs d'un objet

Pour mapper les valeurs d'un objet à l'aide d'une fonction fournie pour générer un nouvel objet avec les mêmes clés, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.keys()` pour itérer sur les clés de l'objet.
3. Utilisez `Array.prototype.reduce()` pour créer un nouvel objet avec les mêmes clés et les valeurs mises en correspondance à l'aide de la fonction `fn` fournie.
4. Le code ci-dessous démontre l'implémentation de la fonction `mapValues`.

```js
const mapValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k] = fn(obj[k], k, obj);
    return acc;
  }, {});
```

Voici un exemple d'utilisation de la fonction `mapValues` :

```js
const users = {
  fred: { user: "fred", age: 40 },
  pebbles: { user: "pebbles", age: 1 }
};
mapValues(users, (u) => u.age); // { fred: 40, pebbles: 1 }
```
