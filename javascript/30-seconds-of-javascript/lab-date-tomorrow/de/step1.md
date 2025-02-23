# Das Datum von Morgen erhalten

Um das Programmieren zu üben, können Sie beginnen, indem Sie das Terminal/SSH öffnen und `node` eingeben. Nachdem Sie das getan haben, können Sie das Datum von morgen mit den folgenden Schritten erhalten:

1. Verwenden Sie den `Date`-Konstruktor, um das aktuelle Datum zu erhalten.
2. Inkrementieren Sie es um eins, indem Sie `Date.prototype.getDate()` verwenden.
3. Setzen Sie den Wert auf das Ergebnis, indem Sie `Date.prototype.setDate()` verwenden.
4. Verwenden Sie `Date.prototype.toISOString()`, um einen String im Format `yyyy-mm-dd` zurückzugeben.

Hier ist der Code, den Sie verwenden können:

```js
const tomorrow = () => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + 1);
  return currentDate.toISOString().split("T")[0];
};
```

Nachdem Sie diesen Code eingegeben haben, können Sie das Datum von morgen erhalten, indem Sie die Funktion `tomorrow()` aufrufen. Beispielsweise wird, wenn das heutige Datum 2018-10-18 ist, die Ausgabe `2018-10-19` sein.
