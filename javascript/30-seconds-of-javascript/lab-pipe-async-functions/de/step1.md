# Wie man asynchrone Funktionen in JavaScript verknüpft

Um mit der Programmierung in JavaScript zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Nachdem Sie sich mit den Grundlagen vertraut gemacht haben, können Sie mit asynchronen Funktionen beginnen.

Die `pipeAsyncFunctions`-Funktion ermöglicht es Ihnen, eine linksbis-rechts-Funktionskomposition mit asynchronen Funktionen durchzuführen. So funktioniert es:

- Die Funktion nimmt beliebig viele asynchrone Funktionen als Argumente entgegen.
- Der Spread-Operator (`...`) wird verwendet, um diese Funktionen als separate Argumente an die `pipeAsyncFunctions`-Funktion zu übergeben.
- Die resultierende Funktion kann beliebig viele Argumente akzeptieren, aber jede der zu kombinierenden Funktionen muss genau ein Argument akzeptieren.
- Die Funktionen können eine Kombination aus normalen Werten, Promises zurückgeben oder `async` sein und durch `await` zurückgeben.
- Die `reduce()`-Methode wird zusammen mit `Promise.prototype.then()` verwendet, um die Funktionskomposition durchzuführen.
- Die `reduce()`-Methode iteriert über die Funktionen, führt jede in Reihe aus und übergibt das Ergebnis einer Funktion an die nächste.
- Das resultierende Promise wird zurückgegeben.

Hier ist ein Beispiel dafür, wie man `pipeAsyncFunctions` verwendet, um eine Zahl zu addieren:

```js
const sum = pipeAsyncFunctions(
  (x) => x + 1,
  (x) => new Promise((resolve) => setTimeout(() => resolve(x + 2), 1000)),
  (x) => x + 3,
  async (x) => (await x) + 4
);
(async () => {
  console.log(await sum(5)); // 15 (nach einer Sekunde)
})();
```

In diesem Beispiel besteht `sum` aus vier Funktionen, die unterschiedliche Werte zur Eingabzahl hinzufügen. Der endgültige Wert von `sum` ist das Ergebnis der sequentiellen Ausführung jeder Funktion, wobei die zweite Funktion eine Verzögerung von einer Sekunde hat. Das `async`-Schlüsselwort wird mit der letzten Funktion verwendet, um die Verwendung von `await` zu ermöglichen.

Durch die Verwendung von `pipeAsyncFunctions` können Sie beliebig viele asynchrone Funktionen leicht zusammenfügen, um komplexere Funktionalität zu schaffen.
