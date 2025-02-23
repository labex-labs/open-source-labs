# Überprüfen, ob ein Datum ein Werktag ist

Um zu überprüfen, ob ein bestimmtes Datum ein Werktag ist, können Sie den folgenden Codeausschnitt verwenden:

```js
const isWeekday = (date = new Date()) => date.getDay() % 6 !== 0;
```

- Diese Funktion verwendet `Date.prototype.getDay()`, um den Wochentag als Zahl (0-6) zu erhalten, wobei Sonntag 0 und Samstag 6 ist.
- Anschließend wird überprüft, ob der Wochentag nicht gleich 0 (Sonntag) oder 6 (Samstag) ist, was bedeutet, dass es ein Werktag ist.
- Wenn kein Datum als Argument angegeben wird, wird das aktuelle Datum als Standard verwendet.

Beispielverwendung:

```js
isWeekday(); // true (wenn das aktuelle Datum ein Werktag ist)
isWeekday(new Date(2021, 5, 28)); // true (wenn das Datum ein Werktag ist)
```
