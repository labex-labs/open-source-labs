# Funktion zum Hinzufügen von Werktagen zu einem angegebenen Datum

Um ein zukünftiges Datum zu berechnen, indem eine bestimmte Anzahl von Werktagen hinzugefügt wird, können Sie die `addWeekDays`-Funktion verwenden. Hier sind die Schritte:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie die `addWeekDays`-Funktion, die zwei Argumente akzeptiert: `startDate` und `count`.
3. `startDate` ist das Datum, ab dem Sie die Werktage hinzufügen möchten.
4. `count` ist die Anzahl der Werktage, die Sie zum Startdatum hinzufügen möchten.
5. Die Funktion konstruiert ein Array mit der `Array.from()`-Methode und setzt die Länge auf die Anzahl der hinzuzufügenden Werktage.
6. Die `Array.prototype.reduce()`-Methode wird verwendet, um das Array zu iterieren, beginnend bei `startDate`, und es mit `Date.prototype.getDate()` und `Date.prototype.setDate()` zu erhöhen.
7. Die Funktion überprüft, ob das aktuelle `date` ein Wochenende ist oder nicht.
8. Wenn das aktuelle `date` ein Wochenende ist, aktualisiert die Funktion es erneut, indem entweder einen oder zwei Tage hinzugefügt werden, um es zu einem Werktag zu machen.
9. Die Funktion nimmt keine offiziellen Feiertage in Betracht.

```js
const addWeekDays = (startDate, count) =>
  Array.from({ length: count }).reduce((date) => {
    date = new Date(date.setDate(date.getDate() + 1));
    if (date.getDay() % 6 === 0)
      date = new Date(date.setDate(date.getDate() + (date.getDay() / 6 + 1)));
    return date;
  }, startDate);
```

Hier sind einige Beispiele dafür, wie Sie die `addWeekDays`-Funktion verwenden können:

```js
addWeekDays(new Date("Oct 09, 2020"), 5); // 'Oct 16, 2020'
addWeekDays(new Date("Oct 12, 2020"), 5); // 'Oct 19, 2020'
```
