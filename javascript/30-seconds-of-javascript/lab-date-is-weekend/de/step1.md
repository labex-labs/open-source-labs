# Überprüfen, ob ein Datum ein Wochenende ist

Um zu überprüfen, ob ein gegebenes Datum ein Wochenende ist, führen Sie die folgenden Schritte aus:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
- Verwenden Sie die `Date.prototype.getDay()`-Methode, um den Wochentag als Zahl (0-6) zu erhalten, wobei Sonntag 0 und Samstag 6 ist.
- Überprüfen Sie, ob der Tag ein Wochenende ist, indem Sie den Modulo-Operator (`%`) verwenden und ihn mit 0 oder 6 vergleichen.
- Weglassen Sie das Argument `d`, um das aktuelle Datum als Standard zu verwenden.

Hier ist ein Beispielcodeausschnitt, den Sie verwenden können:

```js
const isWeekend = (d = new Date()) => d.getDay() % 6 === 0;
```

Um die Funktion zu testen, rufen Sie sie einfach ohne Argument auf:

```js
isWeekend(); // true oder false (abhängig vom aktuellen Datum)
```

Dies wird `true` zurückgeben, wenn das aktuelle Datum ein Wochenende (Samstag oder Sonntag) ist, andernfalls `false`.
