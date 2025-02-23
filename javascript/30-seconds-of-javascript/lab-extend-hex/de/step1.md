# Wie man einen 3-stelligen Farbcode in einen 6-stelligen Farbcode erweitert

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Sie können die folgende Funktion verwenden, um einen 3-stelligen Farbcode in einen 6-stelligen Farbcode zu erweitern:

```js
const extendHex = (shortHex) =>
  "#" +
  shortHex
    .slice(shortHex.startsWith("#") ? 1 : 0)
    .split("")
    .map((x) => x + x)
    .join("");
```

Um einen 3-stelligen RGB-kodierten hexadezimalen Farbcode in die 6-stellige Form zu konvertieren, folgen Sie diesen Schritten:

- Verwenden Sie `Array.prototype.map()`, `String.prototype.split()` und `Array.prototype.join()`, um das gemappte Array zu verbinden.
- Verwenden Sie `Array.prototype.slice()`, um `#` am Anfang der Zeichenkette zu entfernen, da es einmal hinzugefügt wird.

Hier sind einige Beispiele:

```js
extendHex("#03f"); // '#0033ff'
extendHex("05a"); // '#0055aa'
```
