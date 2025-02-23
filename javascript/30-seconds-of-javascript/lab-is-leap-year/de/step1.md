# Code zum Überprüfen eines Schaltjahrs

Um zu überprüfen, ob ein gegebenes `year` ein Schaltjahr ist, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH.
2. Tippen Sie `node`, um zu beginnen, zu programmieren.
3. Verwenden Sie den `Date`-Konstruktor und legen Sie das Datum auf den 29. Februar des gegebenen `year` fest.
4. Überprüfen Sie, ob der Monat gleich `1` ist, indem Sie `Date.prototype.getMonth()` verwenden.
5. Verwenden Sie den folgenden Codeausschnitt, um zu überprüfen, ob ein Jahr ein Schaltjahr ist:

```js
const isLeapYear = (year) => new Date(year, 1, 29).getMonth() === 1;
```

Hier ist ein Beispiel dafür, wie dieser Code verwendet werden kann:

```js
isLeapYear(2019); // false
isLeapYear(2020); // true
```
