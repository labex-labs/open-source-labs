# Conversion de JSON au format CSV

Pour convertir un tableau d'objets en une chaîne de caractères de valeurs séparées par des virgules (CSV) avec des colonnes spécifiées, utilisez la fonction suivante :

```js
const JSONtoCSV = (arr, columns, delimiter = ",") =>
  [
    columns.join(delimiter),
    ...arr.map((obj) =>
      columns.reduce(
        (acc, key) =>
          `${acc}${!acc.length ? "" : delimiter}"${!obj[key] ? "" : obj[key]}"`,
        ""
      )
    )
  ].join("\n");
```

Pour l'utiliser, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Appelez la fonction `JSONtoCSV` avec les arguments suivants :
   - `arr` : un tableau d'objets à convertir.
   - `columns` : un tableau de chaînes de caractères qui spécifient les colonnes à inclure dans la sortie CSV.
   - `delimiter` : une chaîne de caractères optionnelle qui spécifie le délimiteur à utiliser (valeur par défaut est `','`).
3. La fonction retournera une chaîne de caractères CSV qui contient uniquement les colonnes spécifiées et les valeurs des objets.
4. Si aucun délimiteur n'est spécifié, le délimiteur par défaut `','` sera utilisé.
5. Des exemples d'utilisation de la fonction sont fournis dans le bloc de code ci-dessous.

```js
JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"]
); // 'a,b\n"1","2"\n"3","4"\n"6",""\n"","7"'

JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"],
  ";"
); // 'a;b\n"1";"2"\n"3";"4"\n"6";""\n"";"7"'
```
