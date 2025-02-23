# Umwandeln von CSV in ein Array

Um einen comma-separated values (CSV)-String in ein 2D-Array umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu codieren.
2. Verwenden Sie `Array.prototype.indexOf()`, um das erste Zeilenumbruchzeichen (`\n`) zu finden.
3. Verwenden Sie `Array.prototype.slice()`, um die erste Zeile (Titelzeile) zu entfernen, wenn `omitFirstRow` auf `true` gesetzt ist.
4. Verwenden Sie `String.prototype.split()`, um für jede Zeile einen String zu erstellen.
5. Verwenden Sie `String.prototype.split()`, um die Werte in jeder Zeile mit dem angegebenen `Delimiter` zu trennen.
6. Wenn Sie den zweiten Parameter `Delimiter` nicht angeben, wird das Standard-Delimiter `','` verwendet.
7. Wenn Sie den dritten Parameter `omitFirstRow` nicht angeben, wird die erste Zeile (Titelzeile) des CSV-Strings enthalten sein.

Hier ist der Code, um CSV in ein Array umzuwandeln:

```js
const CSVToArray = (data, delimiter = ",", omitFirstRow = false) =>
  data
    .slice(omitFirstRow ? data.indexOf("\n") + 1 : 0)
    .split("\n")
    .map((v) => v.split(delimiter));
```

Sie können die folgenden Beispiele verwenden, um die Funktion zu testen:

```js
CSVToArray("a,b\nc,d"); // [['a', 'b'], ['c', 'd']];
CSVToArray("a;b\nc;d", ";"); // [['a', 'b'], ['c', 'd']];
CSVToArray("col1,col2\na,b\nc,d", ",", true); // [['a', 'b'], ['c', 'd']];
```
