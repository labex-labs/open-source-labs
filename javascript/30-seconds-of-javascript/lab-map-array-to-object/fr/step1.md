# Mapping Array to Object

Pour mapper les valeurs d'un tableau vers un objet en utilisant une fonction, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer la pratique de codage.
2. Utilisez `Array.prototype.reduce()` pour appliquer `fn` à chaque élément de `arr` et combiner les résultats en un objet.
3. Utilisez `el` comme clé pour chaque propriété et le résultat de `fn` comme valeur.

Voici un extrait de code d'exemple :

```js
const mapObject = (arr, fn) =>
  arr.reduce((acc, el, i) => {
    acc[el] = fn(el, i, arr);
    return acc;
  }, {});
```

Vous pouvez utiliser la fonction `mapObject` comme dans cet exemple :

```js
mapObject([1, 2, 3], (a) => a * a); // { 1: 1, 2: 4, 3: 9 }
```
