# JavaScript-Funktion, um die Anzahl der Tage in einem Monat zu erhalten

Um die Anzahl der Tage in einem bestimmten Monat eines gegebenen Jahres mit JavaScript zu ermitteln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Erstellen Sie eine Funktion namens `daysInMonth`, die zwei Parameter akzeptiert: `year` und `month`.
3. Innerhalb der `daysInMonth`-Funktion verwenden Sie den `Date`-Konstruktor, um ein Datumsobjekt aus dem gegebenen `year` und `month` zu erstellen.
4. Setzen Sie den `days`-Parameter auf `0`, um das letzte Datum des vorherigen Monats zu erhalten, da Monate null-indiziert sind.
5. Verwenden Sie `Date.prototype.getDate()`, um die Anzahl der Tage im gegebenen `month` zurückzugeben.
6. Geben Sie die Anzahl der Tage aus der `daysInMonth`-Funktion zurück.

Hier ist der JavaScript-Code für die `daysInMonth`-Funktion:

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

Sie können die `daysInMonth`-Funktion verwenden, um die Anzahl der Tage in jedem Monat eines beliebigen Jahres zu erhalten, wie in diesen Beispielen gezeigt:

```js
daysInMonth(2020, 12); // 31
daysInMonth(2024, 2); // 29
```
