# Fonction pour retourner chaque élément N-ième d'un tableau

Pour retourner chaque élément `n-ième` d'un tableau, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.filter()` pour créer un nouveau tableau qui contient chaque élément `n-ième` d'un tableau donné.
3. Utilisez la fonction suivante pour implémenter l'étape ci-dessus :

```js
const everyNth = (arr, nth) => arr.filter((e, i) => i % nth === nth - 1);
```

4. Pour tester la fonction, utilisez le code suivant :

```js
everyNth([1, 2, 3, 4, 5, 6], 2); // [ 2, 4, 6 ]
```

Cela retournera un nouveau tableau avec chaque deuxième élément du tableau d'entrée.
