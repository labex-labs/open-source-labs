# Funktion, um das letzte Datum eines Monats zurückzugeben

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion gibt das letzte Datum des Monats für das gegebene Datum zurück.

Um dies zu erreichen, folgen Sie diesen Schritten:

1. Verwenden Sie `Date.prototype.getFullYear()` und `Date.prototype.getMonth()`, um das aktuelle Jahr und den aktuellen Monat aus dem gegebenen Datum zu erhalten.
2. Erstellen Sie ein neues Datum mit dem gegebenen Jahr und Monat, in denen Sie um `1` erhöhen, und dem Tag auf `0` gesetzt (letzter Tag des vorherigen Monats). Sie können für diesen Zweck den `Date`-Konstruktor verwenden.
3. Wenn kein Argument an die Funktion übergeben wird, wird standardmäßig das aktuelle Datum verwendet.
4. Geben Sie das letzte Datum des Monats im Format einer Zeichenkettendarstellung des Datums zurück.

Hier ist der Code für die Funktion:

```js
const getLastDateOfMonth = (date = new Date()) => {
  let lastDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
  return lastDate.toISOString().split("T")[0];
};
```

Sie können die Funktion testen, indem Sie sie mit einem Datumobjekt wie folgt aufrufen:

```js
getLastDateOfMonth(new Date("2015-08-11")); // '2015-08-30'
```
