# Verständnis von alphanumerischen Zeichen

Alphanumerische Zeichen bestehen aus den 26 Buchstaben des englischen Alphabets (sowohl die Großbuchstaben A-Z als auch die Kleinbuchstaben a-z) und den 10 Ziffern (0-9). Wenn wir prüfen, ob eine Zeichenkette alphanumerisch ist, überprüfen wir, dass sie nur diese Zeichen und nichts anderes enthält.

In JavaScript können wir mithilfe von regulären Ausdrücken (regular expressions) auf alphanumerische Zeichen prüfen. Reguläre Ausdrücke (regex) sind Muster, die verwendet werden, um Zeichenkombinationen in Zeichenketten zu finden.

Beginnen wir damit, unseren Code-Editor zu öffnen. Im WebIDE navigieren Sie zum Dateiexplorer auf der linken Seite und erstellen Sie eine neue JavaScript-Datei:

1. Klicken Sie mit der rechten Maustaste in der Dateiexplorer-Panel.
2. Wählen Sie "Neue Datei" aus.
3. Benennen Sie die Datei `alphanumeric.js`.

Sobald Sie die Datei erstellt haben, sollte sie automatisch im Editor geöffnet werden. Wenn nicht, klicken Sie auf `alphanumeric.js` im Dateiexplorer, um sie zu öffnen.

![new-file](../assets/screenshot-20250306-K5AOWF7Z@2x.png)

Jetzt geben wir folgenden Code ein:

```javascript
// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  // Using regular expression to check for alphanumeric characters
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Example usage
console.log("Is 'hello123' alphanumeric?", isAlphaNumeric("hello123"));
console.log("Is '123' alphanumeric?", isAlphaNumeric("123"));
console.log("Is 'hello 123' alphanumeric?", isAlphaNumeric("hello 123"));
console.log("Is 'hello@123' alphanumeric?", isAlphaNumeric("hello@123"));
```

Speichern Sie die Datei, indem Sie `Strg+S` drücken oder "Datei" > "Speichern" aus dem Menü auswählen.

Jetzt führen wir diese JavaScript-Datei aus, um die Ausgabe zu sehen. Öffnen Sie das Terminal im WebIDE, indem Sie "Terminal" > "Neues Terminal" aus dem Menü auswählen oder `` Strg+` `` drücken.

Im Terminal führen Sie folgenden Befehl aus:

```bash
node alphanumeric.js
```

Sie sollten folgende Ausgabe sehen:

```
Is 'hello123' alphanumeric? true
Is '123' alphanumeric? true
Is 'hello 123' alphanumeric? false
Is 'hello@123' alphanumeric? false
```

Diese Ausgabe zeigt, dass unsere Funktion `hello123` und `123` korrekt als alphanumerische Zeichenketten identifiziert, während `hello 123` (enthält ein Leerzeichen) und `hello@123` (enthält ein Sonderzeichen @) keine alphanumerischen Zeichenketten sind.
