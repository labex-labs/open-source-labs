# Fonction pour Vérifier si une Valeur est d'un Type Spécifique

Pour vérifier si une valeur fournie est d'un type spécifié, suivez ces étapes :

- Assurez-vous que la valeur n'est pas `undefined` ou `null` en utilisant `Array.prototype.includes()`.
- Utilisez `Object.prototype.constructor` pour comparer la propriété constructeur de la valeur avec le `type` spécifié.
- La fonction `is()` ci-dessous effectue ces vérifications et renvoie `true` si la valeur est du type spécifié, et `false` sinon.

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

Vous pouvez utiliser `is()` pour vérifier si une valeur est de divers types, tels que `Array`, `ArrayBuffer`, `Map`, `RegExp`, `Set`, `WeakMap`, `WeakSet`, `String`, `Number` et `Boolean`. Par exemple :

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
