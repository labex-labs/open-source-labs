# So erhält man die Zeit mit Doppelpunkt aus einem Datumsobjekt

Wenn Sie sich an der Programmierung üben möchten, können Sie beginnen, indem Sie das Terminal/SSH öffnen und `node` eingeben.

Diese Funktion gibt eine Zeichenfolge im Format `HH:MM:SS` aus einem gegebenen `Date`-Objekt zurück.

Um dies zu erreichen, werden die Methoden `Date.prototype.toTimeString()` und `String.prototype.slice()` verwendet, um den `HH:MM:SS`-Teil des `Date`-Objekts zu extrahieren.

Hier ist der Code für die Funktion:

```js
const getColonTimeFromDate = (date) => date.toTimeString().slice(0, 8);
```

Und hier ist ein Beispiel für die Verwendung:

```js
getColonTimeFromDate(new Date()); // '08:38:00'
```
