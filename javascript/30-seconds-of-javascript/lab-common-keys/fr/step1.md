# Conseils pour le codage et la recherche de clés communes

Pour pratiquer le codage, ouvrez le Terminal/SSH et tapez `node`.

Pour trouver les clés communes entre deux objets, suivez ces étapes :

1. Utilisez `Object.keys()` pour obtenir les clés du premier objet.
2. Utilisez `Object.prototype.hasOwnProperty()` pour vérifier si le deuxième objet a une clé qui se trouve dans le premier objet.
3. Utilisez `Array.prototype.filter()` pour filtrer les clés qui ne sont pas dans les deux objets.

Voici un exemple de code :

```js
const commonKeys = (obj1, obj2) =>
  Object.keys(obj1).filter((key) => obj2.hasOwnProperty(key));
```

Vous pouvez tester le code avec cet exemple :

```js
commonKeys({ a: 1, b: 2 }, { a: 2, c: 1 }); // ['a']
```
