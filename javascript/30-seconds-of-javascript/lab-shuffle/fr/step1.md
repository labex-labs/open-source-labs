# Algorithme de mélange de tableau

Pour mélanger un tableau en JavaScript, utilisez l'algorithme de Fisher-Yates. Cet algorithme réordonne aléatoirement les éléments du tableau et renvoie un nouveau tableau.

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici le code pour l'algorithme de Fisher-Yates :

```js
const shuffle = ([...arr]) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr;
};
```

Pour mélanger un tableau, passez-le à la fonction `shuffle` et elle renverra le tableau mélangé. Par exemple :

```js
const foo = [1, 2, 3];
shuffle(foo); // renvoie [2, 3, 1], et foo est toujours [1, 2, 3]
```
