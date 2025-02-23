# Comment mapper un tableau en un objet en JavaScript

Pour mapper un tableau d'objets en un objet en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()` pour mapper le tableau en un objet.
3. Utilisez le paramètre `mapKey` pour mapper les clés de l'objet et le paramètre `mapValue` pour mapper les valeurs.

Voici un extrait de code d'exemple qui montre comment utiliser la fonction `objectify` pour mapper un tableau d'objets en un objet :

```js
const objectify = (arr, mapKey, mapValue = (i) => i) =>
  arr.reduce((acc, item) => {
    acc[mapKey(item)] = mapValue(item);
    return acc;
  }, {});
```

Vous pouvez ensuite utiliser la fonction `objectify` pour mapper un tableau d'objets en un objet de la manière suivante :

```js
const people = [
  { name: "John", age: 42 },
  { name: "Adam", age: 39 }
];

// Map the object array to an object using the name property as keys
objectify(people, (p) => p.name.toLowerCase());
// Sortie : { john: { name: 'John', age: 42 }, adam: { name: 'Adam', age: 39 } }

// Map the object array to an object using the name property as keys and the age property as values
objectify(
  people,
  (p) => p.name.toLowerCase(),
  (p) => p.age
);
// Sortie : { john: 42, adam: 39 }
```
