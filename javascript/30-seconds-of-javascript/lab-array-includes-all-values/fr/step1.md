# Fonction pour vérifier si un tableau inclut toutes les valeurs

Si vous voulez vérifier si tous les éléments d'un tableau `values` sont inclus dans un autre tableau `arr`, vous pouvez utiliser la fonction `includesAll` en JavaScript.

Pour commencer à utiliser la fonction, ouvrez le Terminal/SSH et tapez `node`.

Voici comment fonctionne la fonction `includesAll` :

- Elle utilise les méthodes `Array.prototype.every()` et `Array.prototype.includes()` pour vérifier si tous les éléments de `values` sont inclus dans `arr`.
- Si tous les éléments de `values` sont inclus dans `arr`, la fonction renverra `true`. Sinon, elle renverra `false`.

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

Voici un exemple d'utilisation de la fonction `includesAll` :

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
