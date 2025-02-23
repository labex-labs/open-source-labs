# Zahlenformatierungsfunktion

Um eine Zahl mit der lokalen Zahlenformatierung zu formatieren, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Number.prototype.toLocaleString()`-Methode, um eine Zahl in das lokale Zahlenformat mit Separatoren zu konvertieren.
3. Geben Sie die zu formatierende Zahl als Argument an die Funktion weiter.

Hier ist eine Beispielimplementierung:

```js
const formatNumber = (num) => num.toLocaleString();
```

Und hier sind einige Beispiele für die Verwendung der Funktion:

```js
formatNumber(123456); // '123,456' in `en-US`
formatNumber(15675436903); // '15.675.436.903' in `de-DE`
```
