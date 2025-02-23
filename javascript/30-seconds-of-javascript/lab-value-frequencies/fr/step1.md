# Instructions for Counting Value Frequencies

Pour compter la fréquence des valeurs dans un tableau, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.reduce()` pour mapper les valeurs uniques aux clés d'un objet, en ajoutant aux clés existantes chaque fois qu'une même valeur est rencontrée. Cela créera un objet avec les valeurs uniques du tableau comme clés et leurs fréquences comme valeurs.
3. Le code pour cette opération est le suivant :

```js
const frequencies = (arr) =>
  arr.reduce((a, v) => {
    a[v] = a[v] ? a[v] + 1 : 1;
    return a;
  }, {});
```

4. Pour utiliser cette fonction, appelez `frequencies` en lui passant le tableau en argument. Par exemple :

```js
frequencies(["a", "b", "a", "c", "a", "a", "b"]); // { a: 4, b: 2, c: 1 }
frequencies([..."ball"]); // { b: 1, a: 1, l: 2 }
```

Avec ces instructions, vous pouvez facilement compter la fréquence des valeurs dans n'importe quel tableau donné.
