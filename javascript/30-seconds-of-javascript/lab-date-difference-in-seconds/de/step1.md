# Erste Schritte mit JavaScript-Date-Objekten

JavaScript bietet ein eingebautes `Date`-Objekt, das es uns ermöglicht, mit Daten und Zeiten zu arbeiten. Bevor wir die Differenz zwischen Daten berechnen, lernen wir zunächst, wie man `Date`-Objekte in JavaScript erstellt und damit arbeitet.

## Starten der Node.js-Umgebung

Beginnen wir damit, die interaktive Node.js-Umgebung zu öffnen:

1. Öffnen Sie das Terminal, indem Sie auf das Terminal-Menü oben im WebIDE klicken.
2. Geben Sie den folgenden Befehl ein und drücken Sie die Eingabetaste:

```bash
node
```

Sie sollten jetzt die Node.js-Eingabeaufforderung (`>`) sehen, was darauf hinweist, dass Sie sich in der interaktiven JavaScript-Umgebung befinden. Dadurch können Sie JavaScript-Code direkt im Terminal ausführen.

![node-prompt](../assets/screenshot-20250306-328ScUbO@2x.png)

## Erstellen von Date-Objekten

In JavaScript können wir ein neues `Date`-Objekt auf verschiedene Arten erstellen:

```javascript
// Aktuelles Datum und Uhrzeit
let now = new Date();
console.log(now);

// Bestimmtes Datum und Uhrzeit (Jahr, Monat [0-11], Tag, Stunde, Minute, Sekunde)
let specificDate = new Date(2023, 0, 15, 10, 30, 45); // 15. Januar 2023, 10:30:45
console.log(specificDate);

// Datum aus einem String
let dateFromString = new Date("2023-01-15T10:30:45");
console.log(dateFromString);
```

Versuchen Sie, jedes dieser Beispiele in der Node.js-Umgebung einzugeben und beobachten Sie die Ausgabe.

Beachten Sie, dass in JavaScript die Monate nullbasiert indiziert sind, d. h. Januar ist 0, Februar ist 1 und so weiter.

## Abrufen des Zeitstempels aus Date-Objekten

Jedes `Date`-Objekt in JavaScript speichert intern die Zeit als Anzahl der Millisekunden, die seit dem 1. Januar 1970 (UTC) vergangen sind. Dies wird als Zeitstempel (timestamp) bezeichnet.

```javascript
let now = new Date();
console.log(now.getTime()); // Zeitstempel in Millisekunden abrufen
```

Dieser Zeitstempel wird für die Berechnung der Differenz zwischen Daten nützlich sein.
