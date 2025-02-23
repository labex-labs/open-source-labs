# Conversion d'un objet en un tableau de paires clé-valeur

Pour convertir un objet en un tableau de paires clé-valeur, utilisez la méthode `Object.keys()` et la méthode `Array.prototype.map()`. Cela permettra d'itérer sur les clés de l'objet et de produire un tableau avec des paires clé-valeur. Alternativement, vous pouvez utiliser la méthode `Object.entries()`, qui offre une fonctionnalité similaire.

Voici un extrait de code d'exemple qui montre comment convertir un objet en un tableau de paires clé-valeur :

```js
const objectToEntries = (obj) => Object.keys(obj).map((k) => [k, obj[k]]);
```

Vous pouvez utiliser la fonction `objectToEntries()` pour convertir un objet en un tableau de paires clé-valeur comme ceci :

```js
objectToEntries({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```
