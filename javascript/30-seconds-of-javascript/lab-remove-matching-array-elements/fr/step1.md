# Suppression d'éléments correspondants d'un tableau

Pour supprimer des éléments spécifiques d'un tableau sur la base d'une condition donnée, vous pouvez utiliser la fonction `remove`. Cette fonction modifie le tableau original en supprimant les éléments pour lesquels la fonction donnée renvoie `false`.

Voici les étapes pour utiliser la fonction `remove` :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.filter()` pour trouver les éléments du tableau qui renvoient des valeurs véridiques.
3. Utilisez `Array.prototype.reduce()` pour supprimer les éléments en utilisant `Array.prototype.splice()`.
4. La fonction de rappel est appelée avec trois arguments (valeur, index, tableau).

```js
const remove = (arr, func) =>
  Array.isArray(arr)
    ? arr.filter(func).reduce((acc, val) => {
        arr.splice(arr.indexOf(val), 1);
        return acc.concat(val);
      }, [])
    : [];
```

Voici un exemple d'utilisation de la fonction `remove` :

```js
remove([1, 2, 3, 4], (n) => n % 2 === 0); // [2, 4]
```

Cela renverra un nouveau tableau avec les éléments supprimés.
