# Die Ausführungszeit einer Funktion messen

Um die Ausführungszeit einer Funktion zu messen, verwenden Sie `console.time()` und `console.timeEnd()`, um den Unterschied zwischen Start- und Endzeit zu bestimmen.

Hier ist eine Beispiel-Funktion namens `timeTaken`, die die Ausführungszeit einer Callback-Funktion misst:

```js
const timeTaken = (callback) => {
  console.time("timeTaken");
  const result = callback();
  console.timeEnd("timeTaken");
  return result;
};
```

Um diese Funktion zu verwenden, übergeben Sie einfach Ihre Callback-Funktion als Argument. Beispielsweise:

```js
timeTaken(() => Math.pow(2, 10)); // Gibt 1024 zurück und protokolliert: timeTaken: 0.02099609375ms
```

Im obigen Beispiel wird die `timeTaken`-Funktion verwendet, um die Zeit zu messen, die es dauert, um die `Math.pow(2, 10)`-Funktionsaufruf auszuführen, der 1024 zurückgibt. Die Konsolenausgabe wird die Zeit in Millisekunden (ms) anzeigen.
