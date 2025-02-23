# Zwei-dimensionales Array in CSV umwandeln

Um ein zweidimensionales Array in einen durch Kommas getrennten Wert (CSV)-String umzuwandeln, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.map()` und `Array.prototype.join()`, um einzelne eindimensionale Arrays (Zeilen) zu Strings zusammenzufügen, wobei der bereitgestellte `delimiter` verwendet wird.
3. Verwenden Sie `Array.prototype.join()`, um alle Zeilen zu einem CSV-String zusammenzufügen, wobei jede Zeile durch eine neue Zeile (`\n`) getrennt wird.
4. Wenn Sie den Standardtrennzeichen `,` verwenden möchten, können Sie das zweite Argument `delimiter` weglassen.

Hier ist ein Beispiel für den Code:

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

Sie können die Funktion testen, indem Sie die folgenden Codezeilen ausführen:

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
