# Wie man in JavaScript den Fall eines Strings tauscht

Um in JavaScript den Fall eines Strings zu tauschen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den Spreadoperator (`...`), um den Eingabestring `str` in ein Array von Zeichen umzuwandeln.
3. Verwenden Sie `String.prototype.toLowerCase()` und `String.prototype.toUpperCase()`, um Kleinbuchstaben in Großbuchstaben umzuwandeln und umgekehrt.
4. Verwenden Sie `Array.prototype.map()`, um die Transformation auf jedes Zeichen anzuwenden, und `Array.prototype.join()`, um die Zeichen wieder zu einem String zusammenzufügen.
5. Beachten Sie, dass das Doppelt-Tauschen des Falls eines Strings nicht unbedingt zum ursprünglichen String führt.

Hier ist ein Beispielcodeausschnitt, der zeigt, wie man in JavaScript den Fall eines Strings tauscht:

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // Ausgabe: 'hELLO WORLD!'
```
