# CSV in JSON

Um eine durch Kommata getrennte Werte (CSV)-Zeichenfolge in ein zweidimensionales Array von Objekten umzuwandeln und damit die Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Die erste Zeile der Zeichenfolge wird als Titelzeile verwendet. Hier sind die Schritte, um CSV in JSON umzuwandeln:

1. Verwenden Sie `Array.prototype.indexOf()`, um das erste Zeilenumbruchzeichen (`\n`) zu finden.
2. Verwenden Sie `Array.prototype.slice()`, um die erste Zeile (Titelzeile) zu entfernen und `String.prototype.split()`, um sie in Werte zu trennen, unter Verwendung des angegebenen `Delimiters`.
3. Verwenden Sie `String.prototype.split()`, um für jede Zeile eine Zeichenfolge zu erstellen.
4. Verwenden Sie `String.prototype.split()`, um die Werte in jeder Zeile zu trennen, unter Verwendung des angegebenen `Delimiters`.
5. Verwenden Sie `Array.prototype.reduce()`, um für die Werte jeder Zeile ein Objekt zu erstellen, wobei die Schlüssel aus der Titelzeile extrahiert werden.
6. Lassen Sie das zweite Argument, `Delimiter`, weg, um den Standarddelimiter `,` zu verwenden.

Hier ist der Code:

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

Um die Funktion zu testen, verwenden Sie die folgenden Beispiele:

```js
CSVToJSON("col1,col2\na,b\nc,d");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
CSVToJSON("col1;col2\na;b\nc;d", ";");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
```
