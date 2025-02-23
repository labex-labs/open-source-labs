# JSON in CSV umwandeln

Um ein Array von Objekten in einen als durch Kommas getrennte Werte (CSV) formatierten String mit bestimmten Spalten zu konvertieren, verwenden Sie die folgende Funktion:

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

Um sie zu verwenden, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Rufen Sie die `JSONtoCSV`-Funktion mit den folgenden Argumenten auf:
   - `arr`: Ein Array von Objekten, die konvertiert werden sollen.
   - `columns`: Ein Array von Zeichenketten, die die Spalten angeben, die im CSV-Ausgabe enthalten sein sollen.
   - `delimiter`: Ein optionaler String, der den zu verwendenden Trennzeichen angibt (Standardwert ist `','`).
3. Die Funktion wird einen CSV-String zurückgeben, der nur die angegebenen Spalten und die Werte der Objekte enthält.
4. Wenn kein Trennzeichen angegeben ist, wird das Standardtrennzeichen `','` verwendet.
5. Im folgenden Codeblock werden Beispiele für die Verwendung der Funktion bereitgestellt.

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
