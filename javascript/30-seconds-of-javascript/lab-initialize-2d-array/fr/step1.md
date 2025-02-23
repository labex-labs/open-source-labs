# Initialiser un tableau 2D en JavaScript

Pour initialiser un tableau 2D en JavaScript, vous pouvez utiliser le code suivant :

```js
const initialize2DArray = (width, height, value = null) => {
  return Array.from({ length: height }).map(() =>
    Array.from({ length: width }).fill(value)
  );
};
```

Ce code utilise `Array.from()` et `Array.prototype.map()` pour créer un tableau de `height` lignes, où chaque ligne est un nouveau tableau de longueur `width`. Il utilise également `Array.prototype.fill()` pour définir tous les éléments du tableau sur le paramètre `value`. Si aucune `value` n'est fournie, elle est par défaut `null`.

Vous pouvez appeler la fonction comme ceci :

```js
initialize2DArray(2, 2, 0); // [[0, 0], [0, 0]]
```

Cela créera un tableau 2D avec une largeur de 2, une hauteur de 2 et toutes les valeurs définies sur 0.
