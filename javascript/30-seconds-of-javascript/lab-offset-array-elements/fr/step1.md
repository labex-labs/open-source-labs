# Comment décaler les éléments d'un tableau en JavaScript

Pour déplacer un nombre spécifié d'éléments à la fin d'un tableau JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.slice()` deux fois pour obtenir les éléments après l'index spécifié et les éléments avant cet index.
3. Utilisez l'opérateur de propagation (`...`) pour combiner les deux tableaux en un seul.
4. Si le `décalage` est négatif, les éléments seront déplacés de la fin au début du tableau.

Voici un extrait de code d'exemple qui implémente la fonction `décalage` :

```js
const offset = (arr, offset) => [...arr.slice(offset), ...arr.slice(0, offset)];
```

Vous pouvez ensuite appeler la fonction avec vos tableaux et valeurs de décalage souhaités :

```js
offset([1, 2, 3, 4, 5], 2); // [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2); // [4, 5, 1, 2, 3]
```
