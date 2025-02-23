# Wie man überprüft, ob ein Datum gültig ist

Um zu überprüfen, ob ein Datum gültig ist, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
2. Verwenden Sie den Spread-Operator (`...`), um das Argumentarray an den `Date`-Konstruktor zu übergeben.
3. Verwenden Sie `Date.prototype.valueOf()` und `Number.isNaN()`, um zu überprüfen, ob aus den gegebenen Werten ein gültiges `Date`-Objekt erstellt werden kann.

Hier ist ein Beispielcodeausschnitt:

```js
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());
```

Sie können die Funktion mit verschiedenen Werten testen, wie unten gezeigt:

```js
isDateValid("December 17, 1995 03:24:00"); // true
isDateValid("1995-12-17T03:24:00"); // true
isDateValid("1995-12-17 T03:24:00"); // false
isDateValid("Duck"); // false
isDateValid(1995, 11, 17); // true
isDateValid(1995, 11, 17, "Duck"); // false
isDateValid({}); // false
```
