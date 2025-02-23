# Convertir un tableau 2D en CSV

Pour convertir un tableau 2D en une chaîne de caractères au format valeurs séparées par des virgules (CSV), suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.map()` et `Array.prototype.join()` pour combiner les tableaux 1D individuels (les lignes) en chaînes de caractères, en utilisant le `délimiteur` fourni.
3. Utilisez `Array.prototype.join()` pour combiner toutes les lignes en une chaîne CSV, en séparant chaque ligne par un retour à la ligne (`\n`).
4. Si vous voulez utiliser le délimiteur par défaut `,`, omettez le deuxième argument, `délimiteur`.

Voici un exemple de code :

```js
const arrayToCSV = (arr, delimiter = ",") =>
  arr
    .map((v) =>
      v
        .map((x) => (isNaN(x) ? `"${x.replace(/"/g, '""')}"` : x))
        .join(delimiter)
    )
    .join("\n");
```

Vous pouvez tester la fonction en exécutant les lignes de code suivantes :

```js
arrayToCSV([
  ["a", "b"],
  ["c", "d"]
]); // '"a","b"\n"c","d"'
arrayToCSV(
  [
    ["a", "b"],
    ["c", "d"]
  ],
  ";"
); // '"a";"b"\n"c";"d"'
arrayToCSV([
  ["a", '"b" great'],
  ["c", 3.1415]
]);
// '"a","""b"" great"\n"c",3.1415'
```
