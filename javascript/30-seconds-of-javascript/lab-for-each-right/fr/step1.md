# Voici comment exécuter une fonction pour chaque élément d'un tableau dans l'ordre inverse

Pour exécuter une fonction pour chaque élément d'un tableau, en commençant par le dernier élément du tableau, suivez ces étapes :

1. Clonez le tableau donné en utilisant `Array.prototype.slice()`.
2. Inversez le tableau cloné en utilisant `Array.prototype.reverse()`.
3. Utilisez `Array.prototype.forEach()` pour itérer sur le tableau inversé.

Voici un extrait de code d'exemple :

```js
const forEachRight = (arr, callback) => arr.slice().reverse().forEach(callback);
```

Vous pouvez tester la fonction en exécutant le code suivant :

```js
forEachRight([1, 2, 3, 4], (val) => console.log(val)); // '4', '3', '2', '1'
```

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.
