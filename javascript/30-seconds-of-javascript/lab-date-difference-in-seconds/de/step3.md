# Implementierung der Funktion zur Berechnung der Datumsdifferenz mit Pfeilfunktionen (Arrow Functions)

Nachdem wir nun wissen, wie man Datumsdifferenzen berechnet, implementieren wir eine kompaktere Version unserer Funktion mit Pfeilfunktionen (Arrow Functions).

## Pfeilfunktionen in JavaScript

Pfeilfunktionen bieten eine kürzere Syntax für das Schreiben von Funktionen in JavaScript. So können wir unsere Funktion zur Berechnung der Datumsdifferenz mit der Syntax von Pfeilfunktionen umschreiben:

```javascript
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

Diese Funktion macht genau dasselbe wie unsere vorherige Funktion, aber mit einer saubereren und kompakteren Syntax.

## Erstellen einer JavaScript-Datei

Erstellen wir eine JavaScript-Datei, um unsere Funktion zu speichern und zu testen. Verlassen Sie die Node.js-Umgebung, indem Sie Strg+D drücken oder `.exit` eingeben und die Eingabetaste drücken.

Jetzt erstellen Sie eine neue Datei mit dem Namen `dateDifference.js` im WebIDE:

1. Klicken Sie auf das Symbol "Explorer" in der linken Seitenleiste.
2. Klicken Sie mit der rechten Maustaste im Dateiexplorer und wählen Sie "Neue Datei" aus.
3. Benennen Sie die Datei `dateDifference.js` und drücken Sie die Eingabetaste.
4. Fügen Sie den folgenden Code in die Datei ein:

```javascript
// Funktion zur Berechnung der Differenz zwischen zwei Daten in Sekunden
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Testbeispiele
console.log("Beispiel 1:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:15"),
    new Date("2020-12-24 00:00:17")
  )
); // Erwartete Ausgabe: 2

console.log("\nBeispiel 2:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 00:01:00")
  )
); // Erwartete Ausgabe: 60

console.log("\nBeispiel 3:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 01:00:00")
  )
); // Erwartete Ausgabe: 3600
```

Speichern Sie die Datei, indem Sie Strg+S drücken oder auf Datei > Speichern klicken.

## Ausführen der JavaScript-Datei

Um die Datei, die wir gerade erstellt haben, auszuführen, verwenden Sie den folgenden Befehl im Terminal:

```bash
node dateDifference.js
```

Sie sollten die folgende Ausgabe sehen:

```
Beispiel 1:
2

Beispiel 2:
60

Beispiel 3:
3600
```

Dies bestätigt, dass unsere Funktion korrekt funktioniert:

- Erstes Beispiel: Die Differenz zwischen 00:00:15 und 00:00:17 beträgt 2 Sekunden.
- Zweites Beispiel: Die Differenz zwischen 00:00:00 und 00:01:00 beträgt 60 Sekunden (1 Minute).
- Drittes Beispiel: Die Differenz zwischen 00:00:00 und 01:00:00 beträgt 3600 Sekunden (1 Stunde).
