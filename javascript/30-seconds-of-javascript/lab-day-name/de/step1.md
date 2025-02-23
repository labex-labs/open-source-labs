# Abrufen des Wochentagnamens aus einem Datumsobjekt

Um den Wochentagnamen aus einem `Date`-Objekt abzurufen, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Date.prototype.toLocaleDateString()` mit der Option `{ weekday: 'long' }`, um den Wochentag abzurufen.
3. Sie können das optionale zweite Argument verwenden, um einen sprachspezifischen Namen zu erhalten, oder es weglassen, um die Standardumgebung zu verwenden.

Hier ist eine Beispielimplementierung:

```js
const dayName = (date, locale) =>
  date.toLocaleDateString(locale, { weekday: "long" });
```

Sie können diese Funktion wie folgt verwenden:

```js
dayName(new Date()); // 'Samstag'
dayName(new Date("09/23/2020"), "de-DE"); // 'Samstag'
```
