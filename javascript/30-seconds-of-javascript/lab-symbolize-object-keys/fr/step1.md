# Comment symboliser les clés d'un objet en JavaScript

Pour symboliser les clés d'un objet en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Object.keys()` pour obtenir les clés de l'objet que vous voulez symboliser.
3. Utilisez la méthode `Array.prototype.reduce()` et `Symbol` pour créer un nouvel objet où chaque clé est convertie en un `Symbol`.
4. Voici un extrait de code d'exemple :

```js
const symbolizeKeys = (obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({ ...acc, [Symbol(key)]: obj[key] }),
    {}
  );
```

5. Pour tester la fonction, appelez `symbolizeKeys()` avec votre objet en argument, comme ceci :

```js
symbolizeKeys({ id: 10, name: "apple" });
// { [Symbol(id)]: 10, [Symbol(name)]: 'apple' }
```

En suivant ces étapes, vous pouvez facilement symboliser les clés de n'importe quel objet en JavaScript.
