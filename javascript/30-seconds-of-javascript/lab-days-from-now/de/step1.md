# Funktion, um das Datum von heute aus für 'n' Tage zu berechnen

Um das Datum von heute aus für 'n' Tage zu berechnen, gehen Sie folgendermaßen vor:

- Öffnen Sie das Terminal/SSH und geben Sie 'node' ein, um mit der Programmierung zu beginnen.
- Verwenden Sie den `Date`-Konstruktor, um das aktuelle Datum zu erhalten.
- Verwenden Sie `Math.abs()` und `Date.prototype.getDate()`, um das Datum entsprechend zu aktualisieren.
- Setzen Sie das Ergebnis mit `Date.prototype.setDate()`.
- Verwenden Sie `Date.prototype.toISOString()`, um eine Zeichenfolge im Format `yyyy-mm-dd` zurückzugeben.

Hier ist der Code:

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

Beispielverwendung:

```js
daysFromNow(5); // Ausgabe: 2020-10-13 (wenn das aktuelle Datum 2020-10-08 ist)
```
