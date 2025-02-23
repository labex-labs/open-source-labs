# Comment mapper un objet en un tableau en JavaScript

Pour mapper un objet en un tableau en JavaScript, vous pouvez utiliser la fonction `listify()`. Voici comment faire :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. Utilisez `Object.entries()` pour obtenir un tableau des paires clé-valeur de l'objet.

3. Utilisez `Array.prototype.reduce()` pour mapper le tableau en un objet.

4. Utilisez `mapFn` pour mapper les clés et les valeurs de l'objet et `Array.prototype.push()` pour ajouter les valeurs mappées au tableau.

Voici le code de la fonction `listify()` :

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

Et voici un exemple de manière à l'utiliser avec un objet appelé `people` :

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

Avec cette fonction, vous pouvez facilement mapper un objet en un tableau en JavaScript.
