# Fonction pour indexer un tableau

Pour indexer un tableau à l'aide d'une fonction, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()` pour créer un objet à partir du tableau.
3. Appliquez la fonction fournie à chaque valeur du tableau pour produire une clé et ajoutez la paire clé-valeur à l'objet.

Voici un extrait de code d'exemple :

```js
const indexBy = (arr, fn) =>
  arr.reduce((obj, v, i) => {
    obj[fn(v, i, arr)] = v;
    return obj;
  }, {});
```

Vous pouvez utiliser cette fonction comme suit :

```js
indexBy(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  (x) => x.id
);
// { '10': { id: 10, name: 'apple' }, '20': { id: 20, name: 'orange' } }
```

Cette fonction crée un objet à partir d'un tableau en assignant à chaque valeur une clé à l'aide d'une fonction fournie. L'objet résultant contient des paires clé-valeur où les clés sont produites par la fonction et les valeurs sont les éléments d'origine du tableau.
