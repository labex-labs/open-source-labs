# Funktion zum Hinzufügen von Tagen zu einem Datum

Hier ist eine Funktion, die das Datum von `n` Tagen ab dem angegebenen Datum berechnen und seine String-Darstellung zurückgeben kann.

Um die Funktion zu verwenden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie den `Date`-Konstruktor, um ein `Date`-Objekt aus dem ersten Argument zu erstellen.
3. Verwenden Sie `Date.prototype.getDate()` und `Date.prototype.setDate()`, um `n` Tage zum angegebenen Datum hinzuzufügen.
4. Verwenden Sie `Date.prototype.toISOString()`, um einen String im Format `yyyy-mm-dd` zurückzugeben.

Hier ist der Code für die Funktion:

```js
const addDaysToDate = (date, n) => {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d.toISOString().split("T")[0];
};
```

Sie können die Funktion mit den folgenden Beispielen testen:

```js
addDaysToDate("2020-10-15", 10); // '2020-10-25'
addDaysToDate("2020-10-15", -10); // '2020-10-05'
```
