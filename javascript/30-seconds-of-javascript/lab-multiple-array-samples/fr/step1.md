# Code Practice: Getting Random Elements from an Array

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Le code suivant utilise l'algorithme de Fisher-Yates pour mélanger un tableau et récupérer `n` éléments aléatoires et uniques à des clés uniques dans le tableau, jusqu'à la taille du tableau.

```js
const sampleSize = ([...arr], n = 1) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr.slice(0, n);
};
```

Pour utiliser ce code, appelez `sampleSize()` avec un tableau et un nombre optionnel `n` d'éléments à récupérer. Si `n` n'est pas fourni, la fonction retournera seulement un élément au hasard dans le tableau.

```js
sampleSize([1, 2, 3], 2); // [3, 1]
sampleSize([1, 2, 3], 4); // [2, 3, 1]
```
