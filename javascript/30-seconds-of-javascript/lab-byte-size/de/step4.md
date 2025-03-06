# Erstellen einer praktischen Beispiel-Datei

Jetzt erstellen wir eine JavaScript-Datei, um unsere Funktion zur Berechnung der Byte-Größe auf praktische Weise umzusetzen. Dies zeigt, wie Sie diese Funktion in einer realen Anwendung verwenden könnten.

1. Erstellen Sie eine neue Datei im WebIDE. Klicken Sie auf das Symbol "Neue Datei" in der Datei-Explorer-Sidebar und benennen Sie sie `byteSizeCalculator.js`.

2. Fügen Sie den folgenden Code in die Datei ein:

```javascript
/**
 * Calculate the byte size of a given string.
 * @param {string} str - The string to calculate the byte size for.
 * @returns {number} The size in bytes.
 */
function calculateByteSize(str) {
  return new Blob([str]).size;
}

// Examples with different types of strings
const examples = [
  "Hello World",
  "😀",
  "The quick brown fox jumps over the lazy dog",
  "123!@#$%^&*()",
  "Hello, 世界!",
  "😀😃😄😁"
];

// Display the results
console.log("String Byte Size Calculator\n");
console.log("String".padEnd(45) + "| Characters | Bytes");
console.log("-".repeat(70));

examples.forEach((example) => {
  console.log(
    `"${example}"`.padEnd(45) +
      `| ${example.length}`.padEnd(12) +
      `| ${calculateByteSize(example)}`
  );
});
```

3. Speichern Sie die Datei, indem Sie Strg+S drücken oder über das Menü Datei > Speichern auswählen.

4. Führen Sie die Datei über das Terminal aus:

```bash
node byteSizeCalculator.js
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
String Byte Size Calculator

String                                      | Characters | Bytes
----------------------------------------------------------------------
"Hello World"                               | 11         | 11
"😀"                                        | 1          | 4
"The quick brown fox jumps over the lazy dog" | 43         | 43
"123!@#$%^&*()"                            | 13         | 13
"Hello, 世界!"                              | 10         | 13
"😀😃😄😁"                                  | 4          | 16
```

Diese Tabelle zeigt deutlich den Unterschied zwischen der Anzahl der Zeichen und der Byte-Größe für verschiedene Arten von Zeichenketten.

Das Verständnis dieser Unterschiede ist entscheidend, wenn:

- Sie Grenzwerte für Benutzereingaben in Webformularen festlegen
- Sie die Speicheranforderungen für Textdaten berechnen
- Sie mit APIs arbeiten, die Größenbeschränkungen haben
- Sie die Datenübertragung über Netzwerke optimieren
