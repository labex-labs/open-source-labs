# Comment obtenir la queue d'un tableau en JavaScript

Pour obtenir tous les éléments d'un tableau sauf le premier, vous pouvez utiliser la méthode `Array.prototype.slice()`. Si la longueur du tableau est supérieure à 1, utilisez `slice(1)` pour renvoyer le tableau sans le premier élément. Sinon, renvoyez le tableau entier.

Alors que le découpage négatif (comme `slice(-4)`) est possible en JavaScript et effectue un découpage à partir de la fin, nous utilisons `slice(1)` ici car :

1. Cela communique clairement notre intention de sauter le premier élément
2. Cela fonctionne de manière cohérente indépendamment de la longueur du tableau
3. Le découpage négatif nécessiterait de connaître la longueur du tableau pour obtenir le même résultat

Voici un exemple de code :

```js
const tail = (arr) => (arr.length > 1 ? arr.slice(1) : arr);
```

Vous pouvez maintenant utiliser la fonction `tail()` pour obtenir la queue du tableau :

```js
tail([1, 2, 3]); // [2, 3]
tail([1]); // [1]
```
