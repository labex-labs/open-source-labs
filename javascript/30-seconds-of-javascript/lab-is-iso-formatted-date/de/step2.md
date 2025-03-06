# Erstellen einer Funktion zur Validierung von ISO-formatierte Datumszeichenketten

In diesem Schritt werden wir eine JavaScript-Funktion erstellen, die prüft, ob eine gegebene Zeichenkette im gültigen ISO 8601-Format vorliegt.

## Erstellen der Validierungsfunktion

Erstellen wir eine neue JavaScript-Datei für unseren ISO-Datum-Validator:

1. Klicken Sie im WebIDE auf das Explorer-Symbol in der linken Seitenleiste.
2. Klicken Sie mit der rechten Maustaste im Dateiexplorer und wählen Sie "Neue Datei".
3. Benennen Sie die Datei `isISODate.js` und drücken Sie die Eingabetaste.
4. Fügen Sie den folgenden Code zur Datei hinzu:

```javascript
/**
 * Checks if a string is a valid ISO 8601 formatted date string
 * @param {string} val - The string to check
 * @return {boolean} - Returns true if the string is in ISO format, false otherwise
 */
const isISOString = (val) => {
  // Create a Date object from the input string
  const d = new Date(val);

  // Check if the date is valid (not NaN) and if the ISO string matches the original
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// Export the function so we can use it elsewhere
module.exports = isISOString;
```

Untersuchen wir, wie diese Funktion funktioniert:

1. `new Date(val)` erstellt ein Date-Objekt aus der Eingabezeichenkette.
2. `d.valueOf()` gibt den numerischen Zeitstempelwert (Millisekunden seit dem 1. Januar 1970) zurück.
3. `Number.isNaN(d.valueOf())` prüft, ob das Datum ungültig ist (NaN steht für "Not a Number").
4. `d.toISOString() === val` überprüft, ob das Konvertieren des Date-Objekts zurück in eine ISO-Zeichenkette mit der ursprünglichen Eingabe übereinstimmt.

## Testen unserer Funktion

Jetzt erstellen wir eine einfache Testdatei, um unsere Funktion zu testen:

1. Erstellen Sie eine weitere Datei mit dem Namen `testISO.js`.
2. Fügen Sie den folgenden Code hinzu:

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Test with a valid ISO formatted date
console.log("Testing a valid ISO date:");
console.log("2020-10-12T10:10:10.000Z");
console.log("Result:", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// Test with an invalid format
console.log("Testing a non-ISO date:");
console.log("2020-10-12");
console.log("Result:", isISOString("2020-10-12"));
```

3. Führen Sie die Testdatei mit Node.js aus:

```bash
node testISO.js
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Testing a valid ISO date:
2020-10-12T10:10:10.000Z
Result: true

Testing a non-ISO date:
2020-10-12
Result: false
```

Dies zeigt, dass unsere Funktion korrekt erkennt, dass "2020-10-12T10:10:10.000Z" ein gültiges ISO-formatiertes Datum ist, während "2020-10-12" es nicht ist.
