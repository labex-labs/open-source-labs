# CSV vers JSON

Pour convertir une chaîne de caractères au format valeurs séparées par des virgules (CSV) en un tableau 2D d'objets et l'utiliser pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. La première ligne de la chaîne est utilisée comme ligne de titres. Voici les étapes pour convertir le CSV en JSON :

1. Utilisez `Array.prototype.indexOf()` pour trouver le premier caractère de nouvelle ligne (`\n`).
2. Utilisez `Array.prototype.slice()` pour supprimer la première ligne (ligne de titres) et `String.prototype.split()` pour la séparer en valeurs, en utilisant le `délimiteur` fourni.
3. Utilisez `String.prototype.split()` pour créer une chaîne pour chaque ligne.
4. Utilisez `String.prototype.split()` pour séparer les valeurs dans chaque ligne, en utilisant le `délimiteur` fourni.
5. Utilisez `Array.prototype.reduce()` pour créer un objet pour les valeurs de chaque ligne, avec les clés extraites de la ligne de titres.
6. Omettez le second argument, `délimiteur`, pour utiliser un délimiteur par défaut de `,`.

Voici le code :

```js
const CSVToJSON = (data, delimiter = ",") => {
  const titles = data.slice(0, data.indexOf("\n")).split(delimiter);
  return data
    .slice(data.indexOf("\n") + 1)
    .split("\n")
    .map((v) => {
      const values = v.split(delimiter);
      return titles.reduce(
        (obj, title, index) => ((obj[title] = values[index]), obj),
        {}
      );
    });
};
```

Pour tester la fonction, utilisez les exemples suivants :

```js
CSVToJSON("col1,col2\na,b\nc,d");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
CSVToJSON("col1;col2\na;b\nc;d", ";");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
```
