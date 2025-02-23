# Datum in das ISO-Format mit Zeitzone umwandeln

Um ein Datum in das erweiterte ISO-Format (ISO 8601), einschließlich der Zeitzonenverschiebung, umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen zu codieren.
2. Verwenden Sie `Date.prototype.getTimezoneOffset()`, um die Zeitzonenverschiebung zu erhalten und umzukehren. Speichern Sie das Vorzeichen in `diff`.
3. Definieren Sie eine Hilfsfunktion, `pad()`, die jede übergebene Zahl mit `Math.floor()` und `Math.abs()` zu einem Integer normalisiert und mit `String.prototype.padStart()` auf `2` Stellen aufrundet.
4. Verwenden Sie `pad()` und die integrierten Methoden im `Date`-Prototype, um den ISO 8601-String mit Zeitzonenverschiebung zu erstellen.

Hier ist der Code, den Sie verwenden können:

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

Verwenden Sie die Funktion `toISOStringWithTimezone()` mit einem `new Date()`-Objekt als Argument, um das Datum im ISO-Format mit Zeitzonenverschiebung zu erhalten. Beispiel:

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
