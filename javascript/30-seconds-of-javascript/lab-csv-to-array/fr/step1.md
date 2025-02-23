# Conversion d'un CSV en un tableau

Pour convertir une chaîne de caractères au format valeurs séparées par des virgules (CSV) en un tableau 2D, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.
2. Utilisez `Array.prototype.indexOf()` pour localiser le premier caractère de nouvelle ligne (`\n`).
3. Utilisez `Array.prototype.slice()` pour supprimer la première ligne (ligne de titre) si `omitFirstRow` est défini sur `true`.
4. Utilisez `String.prototype.split()` pour créer une chaîne pour chaque ligne.
5. Utilisez `String.prototype.split()` pour séparer les valeurs dans chaque ligne en utilisant le `délimiteur` fourni.
6. Si vous ne fournissez pas le deuxième argument, `délimiteur`, le délimiteur par défaut `','` sera utilisé.
7. Si vous ne fournissez pas le troisième argument, `omitFirstRow`, la première ligne (ligne de titre) de la chaîne CSV sera incluse.

Voici le code pour convertir un CSV en un tableau :

```js
const CSVToArray = (data, delimiter = ",", omitFirstRow = false) =>
  data
    .slice(omitFirstRow ? data.indexOf("\n") + 1 : 0)
    .split("\n")
    .map((v) => v.split(delimiter));
```

Vous pouvez utiliser les exemples suivants pour tester la fonction :

```js
CSVToArray("a,b\nc,d"); // [['a', 'b'], ['c', 'd']];
CSVToArray("a;b\nc;d", ";"); // [['a', 'b'], ['c', 'd']];
CSVToArray("col1,col2\na,b\nc,d", ",", true); // [['a', 'b'], ['c', 'd']];
```
