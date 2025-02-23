# JavaScript-Funktion, um die Anzahl der vergangenen Tage zu berechnen

Hier ist eine JavaScript-Funktion, die das Datum von `n` Tagen zurück von heute berechnet und es als Zeichenfolge im Format `yyyy-mm-dd` zurückgibt:

```js
const daysAgo = (n) => {
  const today = new Date();
  const daysAgoDate = new Date(today.setDate(today.getDate() - Math.abs(n)));
  return daysAgoDate.toISOString().split("T")[0];
};
```

So funktioniert es:

- Der `Date`-Konstruktor wird verwendet, um das aktuelle Datum zu erhalten.
- Die `Math.abs()`-Funktion wird verwendet, um sicherzustellen, dass die Anzahl der Tage positiv ist.
- Die `Date.prototype.getDate()`-Funktion wird verwendet, um den Tag des Monats für das aktuelle Datum zu erhalten.
- Die `Date.prototype.setDate()`-Funktion wird verwendet, um das Datum entsprechend zu aktualisieren.
- Das resultierende Datum wird als Zeichenfolge im Format `yyyy-mm-dd` mithilfe der `Date.prototype.toISOString()`-Funktion zurückgegeben.

Beispielverwendung:

```js
daysAgo(20); // "2020-09-16" (wenn das aktuelle Datum 2020-10-06 ist)
```
