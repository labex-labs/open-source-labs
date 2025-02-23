# Konvergierende Funktionen

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion `converge` nimmt eine konvergierende Funktion und eine Liste von Verzweigungsfunktionen als Eingabe entgegen. Sie gibt eine neue Funktion zurück, die jede Verzweigungsfunktion auf die Eingabeargumente anwendet. Die Ergebnisse der Verzweigungsfunktionen werden dann als Argumente an die konvergierende Funktion übergeben.

Die Methoden `Array.prototype.map()` und `Function.prototype.apply()` werden verwendet, um jede Funktion auf die Eingabeargumente anzuwenden. Anschließend wird der Spread-Operator (`...`) verwendet, um `converger` mit den Ergebnissen aller anderen Funktionen aufzurufen.

Hier ist der Code für die `converge`-Funktion:

```js
const converge =
  (converger, fns) =>
  (...args) =>
    converger(...fns.map((fn) => fn.apply(null, args)));
```

Ein Beispiel für die Verwendung dieser Funktion wird unten gezeigt. Die `average`-Funktion wird erstellt, indem `converge` mit einer anonymen Funktion aufgerufen wird, die den Mittelwert eines Arrays berechnet. Die Verzweigungsfunktionen sind zwei anonyme Funktionen, die jeweils die Summe eines Arrays und seine Länge berechnen.

```js
const average = converge(
  (a, b) => a / b,
  [(arr) => arr.reduce((a, v) => a + v, 0), (arr) => arr.length]
);
average([1, 2, 3, 4, 5, 6, 7]); // 4
```

Dieser Code berechnet den Mittelwert des Arrays `[1, 2, 3, 4, 5, 6, 7]` und gibt `4` zurück.
