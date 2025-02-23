# Überprüfen, ob zwei Daten gleich sind

Um zu überprüfen, ob zwei Daten gleich sind, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Date.prototype.toISOString()` und eine strikte Gleichheitsüberprüfung (`===`), um die beiden Daten zu vergleichen.
3. Hier ist ein Beispielcodeausschnitt:

```js
const isSameDate = (dateA, dateB) =>
  dateA.toISOString() === dateB.toISOString();
```

4. Testen Sie die Funktion mit zwei Daten als Argumenten, um zu sehen, ob sie gleich sind:

```js
isSameDate(new Date(2010, 10, 20), new Date(2010, 10, 20)); // true
```

Diese Funktion überprüft, ob die beiden Daten gleich sind, indem sie ihre ISO-String-Darstellungen vergleicht.
