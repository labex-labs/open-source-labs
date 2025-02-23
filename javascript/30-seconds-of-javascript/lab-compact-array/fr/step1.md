# Comment utiliser Array.prototype.filter() pour créer un tableau compact

Pour créer un tableau compact en JavaScript, vous pouvez utiliser la méthode `Array.prototype.filter()` pour supprimer toutes les valeurs fausses du tableau. Les valeurs fausses incluent `false`, `null`, `0`, `""`, `undefined` et `NaN`.

Voici un extrait de code d'exemple qui montre comment créer un tableau compact en utilisant `Array.prototype.filter()` :

```js
const compact = (arr) => arr.filter(Boolean);
```

Vous pouvez ensuite utiliser la fonction `compact` pour créer un tableau compact en passant un tableau en tant qu'argument. Par exemple :

```js
compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]);
// Sortie : [ 1, 2, 3, 'a','s', 34 ]
```

En utilisant `Array.prototype.filter()` de cette manière, vous pouvez facilement créer un tableau compact qui ne contient que des valeurs véridiques.
