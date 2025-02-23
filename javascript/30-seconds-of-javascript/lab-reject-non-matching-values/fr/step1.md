# Filtrer les valeurs d'un tableau

Pour filtrer un tableau en fonction d'une fonction prédicat et ne renvoyer que les valeurs pour lesquelles la fonction prédicat renvoie `false`, suivez ces étapes :

1. Utilisez `Array.prototype.filter()` en combinaison avec la fonction prédicat, `pred`.
2. La méthode `filter` ne renverra que les valeurs pour lesquelles la fonction prédicat renvoie `false`.
3. Pour rejeter les valeurs non correspondantes, passez la fonction prédicat et le tableau à la fonction `reject()`.

```js
const reject = (pred, array) => array.filter((...args) => !pred(...args));
```

Voici quelques exemples d'utilisation de la fonction `reject()` :

```js
reject((x) => x % 2 === 0, [1, 2, 3, 4, 5]); // [1, 3, 5]
reject((word) => word.length > 4, ["Apple", "Pear", "Kiwi", "Banana"]);
// ['Pear', 'Kiwi']
```

En suivant ces étapes, vous pouvez facilement filtrer un tableau en fonction d'une fonction prédicat et rejeter les valeurs non correspondantes.
