# Wie man den Unix-Timestamp aus einem Datum in JavaScript bekommt

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Sie können die folgenden Schritte verwenden, um den Unix-Timestamp aus einem `Date`-Objekt in JavaScript zu erhalten:

1. Verwenden Sie `Date.prototype.getTime()`, um den Timestamp in Millisekunden zu erhalten.
2. Teilen Sie den Timestamp durch `1000`, um den Timestamp in Sekunden zu erhalten.
3. Verwenden Sie `Math.floor()`, um den resultierenden Timestamp auf eine Ganzzahl zu runden.
4. Wenn Sie das `date`-Argument weglassen, wird das aktuelle Datum verwendet.

Hier ist ein Beispielcodeausschnitt:

```js
const getTimestamp = (date = new Date()) => Math.floor(date.getTime() / 1000);
```

Sie können die `getTimestamp()`-Funktion aufrufen, um den Unix-Timestamp zu erhalten. Beispielsweise:

```js
getTimestamp(); // 1602162242
```
