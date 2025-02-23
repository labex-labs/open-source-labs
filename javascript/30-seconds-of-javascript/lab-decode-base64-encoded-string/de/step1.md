# Dekodierung einer Base64-codierten Zeichenfolge

Um eine Zeichenfolge von Daten zu dekodieren, die mit Base-64-Codierung codiert wurde, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Erstellen Sie einen `Buffer` für die gegebene Zeichenfolge mit Base-64-Codierung.
3. Verwenden Sie `Buffer.prototype.toString()`, um die dekodierte Zeichenfolge zurückzugeben.

Hier ist ein Beispielcodeausschnitt:

```js
const atob = (str) => Buffer.from(str, "base64").toString("binary");
```

Sie können diese Funktion testen, indem Sie `atob('Zm9vYmFy')` ausführen, was `'foobar'` zurückgeben sollte.
