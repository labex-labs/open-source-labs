# Verständnis von Datumsberechnungen in JavaScript

Nachdem wir nun wissen, wie man `Date`-Objekte erstellt, lernen wir, wie man die Differenz zwischen zwei Daten berechnet.

## Datumsarithmetik in JavaScript

JavaScript ermöglicht es Ihnen, arithmetische Operationen direkt auf `Date`-Objekten auszuführen. Wenn Sie ein `Date`-Objekt von einem anderen subtrahieren, wandelt JavaScript diese automatisch in Zeitstempel (Millisekunden) um und führt die Subtraktion durch.

```javascript
let date1 = new Date("2023-01-01T00:00:00");
let date2 = new Date("2023-01-01T00:01:00");

let differenceInMilliseconds = date2 - date1;
console.log(differenceInMilliseconds); // 60000 (60 Sekunden * 1000 Millisekunden)
```

Versuchen Sie, diesen Code in Ihrer Node.js-Umgebung auszuführen. Das Ergebnis sollte `60000` sein, was 60 Sekunden in Millisekunden darstellt.

## Umrechnen von Millisekunden in Sekunden

Um eine Zeitdifferenz von Millisekunden in Sekunden umzurechnen, teilen wir einfach durch 1000:

```javascript
let differenceInSeconds = differenceInMilliseconds / 1000;
console.log(differenceInSeconds); // 60
```

Dadurch erhalten wir unsere Zeitdifferenz in Sekunden, was in diesem Beispiel 60 Sekunden oder 1 Minute ist.

## Erstellen einer Funktion zur Berechnung der Datumsdifferenz

Nachdem wir das Konzept verstanden haben, erstellen wir eine einfache Funktion, um die Differenz zwischen zwei Daten in Sekunden zu berechnen:

```javascript
function getDateDifferenceInSeconds(startDate, endDate) {
  return (endDate - startDate) / 1000;
}

// Testen Sie die Funktion
let start = new Date("2023-01-01T00:00:00");
let end = new Date("2023-01-01T00:01:30");
let difference = getDateDifferenceInSeconds(start, end);
console.log(difference); // 90 (1 Minute und 30 Sekunden)
```

Versuchen Sie, diese Funktion in der Node.js-Umgebung einzugeben und auszuführen. Das Ergebnis sollte `90` sein, was 1 Minute und 30 Sekunden darstellt.
