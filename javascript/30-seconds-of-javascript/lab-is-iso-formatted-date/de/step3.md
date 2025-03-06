# Testen mit verschiedenen Datumsformaten

Nachdem wir nun unsere grundlegende Validierungsfunktion haben, lassen Sie uns sie mit verschiedenen Datumsformaten testen, um zu verstehen, wie sie auf verschiedene Eingaben reagiert.

## Erstellen einer Testsuite

Erstellen wir eine umfassende Testsuite, um verschiedene Datumsformate zu untersuchen:

1. Erstellen Sie eine neue Datei mit dem Namen `dateTester.js`.
2. Fügen Sie den folgenden Code hinzu:

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Function to test different date strings
function testDate(description, dateString) {
  console.log(`Testing: ${description}`);
  console.log(`Input: "${dateString}"`);
  console.log(`Is ISO Format: ${isISOString(dateString)}`);
  console.log("-----------------------");
}

// Valid ISO date examples
testDate("Standard ISO date with timezone Z", "2023-05-12T14:30:15.123Z");
testDate("ISO date with zero milliseconds", "2020-10-12T10:10:10.000Z");

// Invalid or non-ISO format examples
testDate("Date only (no time component)", "2023-05-12");
testDate("Date and time without milliseconds", "2023-05-12T14:30:15Z");
testDate(
  "Date with time zone offset instead of Z",
  "2023-05-12T14:30:15+01:00"
);
testDate("Invalid date (month 13 does not exist)", "2023-13-12T14:30:15.123Z");
testDate("Non-date string", "Hello World");
```

3. Führen Sie die Testsuite im Terminal aus:

```bash
node dateTester.js
```

Sie sollten eine Ausgabe sehen, die zeigt, welche Zeichenketten gültige ISO-Daten sind und welche nicht.

## Verständnis der Ergebnisse

Lassen Sie uns analysieren, was jeden Testfall gültig oder ungültig macht:

1. `2023-05-12T14:30:15.123Z` – Dies ist gültig, da es dem vollständigen ISO 8601-Format mit dem UTC-Zeitzonenindikator (Z) entspricht.

2. `2020-10-12T10:10:10.000Z` – Dies ist ebenfalls gültig, wobei die Millisekunden explizit auf 000 gesetzt sind.

3. `2023-05-12` – Dies ist ein gültiges Datum, aber nicht im ISO-Format, da der Zeitanteil fehlt.

4. `2023-05-12T14:30:15Z` – Dies scheint ein ISO-Format zu sein, fehlt aber an den Millisekunden, die im strengen ISO-Format erforderlich sind.

5. `2023-05-12T14:30:15+01:00` – Hier wird ein Zeitzonenoffset (+01:00) anstelle von 'Z' verwendet. Obwohl dies gemäß ISO 8601 gültig ist, erfordert unsere Funktion das genaue Format, das von `toISOString()` erzeugt wird, das immer 'Z' verwendet.

6. `2023-13-12T14:30:15.123Z` – Dies ist ein ungültiges Datum (der Monat 13 existiert nicht), daher wird `new Date()` ein ungültiges Date-Objekt erstellen.

7. `Hello World` – Dies ist überhaupt kein Datum, daher wird `new Date()` ein ungültiges Date-Objekt erstellen.

Unsere Validierungsfunktion prüft speziell zwei Bedingungen:

1. Die Zeichenkette muss zu einem gültigen Datum geparst werden (nicht NaN).
2. Wenn dieses Datum wieder in eine ISO-Zeichenkette umgewandelt wird, muss es exakt mit der ursprünglichen Eingabe übereinstimmen.

Dieser Ansatz stellt sicher, dass wir das genaue ISO-Format validieren, das von JavaScripts `toISOString()`-Methode erzeugt wird.
