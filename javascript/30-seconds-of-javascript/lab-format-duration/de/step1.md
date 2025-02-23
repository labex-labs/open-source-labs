# Format-Dauer

Um das menschenlesbare Format einer gegebenen Anzahl von Millisekunden zu erhalten, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Teilen Sie die `ms` mit passenden Werten, um die passenden Werte für `Tag`, `Stunde`, `Minute`, `Sekunde` und `Millisekunde` zu erhalten.
3. Verwenden Sie `Object.entries()` mit `Array.prototype.filter()`, um nur die nicht null-Werte zu behalten.
4. Erstellen Sie den String für jeden Wert, indem Sie die Pluralform entsprechend verwenden, mit `Array.prototype.map()`.
5. Verbinden Sie die Werte zu einem String, indem Sie `Array.prototype.join()` verwenden.

Hier ist der Code:

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

Hier sind einige Beispiele:

```js
formatDuration(1001); // '1 Sekunde, 1 Millisekunde'
formatDuration(34325055574);
// '397 Tage, 6 Stunden, 44 Minuten, 15 Sekunden, 574 Millisekunden'
```
