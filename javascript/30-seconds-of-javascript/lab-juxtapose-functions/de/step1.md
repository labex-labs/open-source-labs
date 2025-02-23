# Erklärung von Juxtapose-Funktionen

Um die `juxt`-Funktion zu verwenden, öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen. Die `juxt`-Funktion nimmt mehrere Funktionen als Argumente entgegen und gibt eine Funktion zurück, die die Verkettung dieser Funktionen darstellt.

Um die `juxt`-Funktion zu erstellen, verwenden Sie `Array.prototype.map()`, um eine `fn` zurückzugeben, die eine variable Anzahl von `args` akzeptieren kann. Wenn `fn` aufgerufen wird, sollte sie ein Array zurückgeben, das das Ergebnis enthält, wenn jede `fn` auf die `args` angewendet wird.

Hier ist eine Beispielimplementierung der `juxt`-Funktion:

```js
const juxt =
  (...fns) =>
  (...args) =>
    [...fns].map((fn) => [...args].map(fn));
```

Sobald Sie die `juxt`-Funktion definiert haben, können Sie sie verwenden, indem Sie beliebig viele Funktionen als Argumente übergeben, gefolgt von beliebig vielen Argumenten, die an diese Funktionen übergeben werden sollen.

Hier sind ein paar Beispiele für die Verwendung der `juxt`-Funktion:

```js
juxt(
  (x) => x + 1,
  (x) => x - 1,
  (x) => x * 10
)(1, 2, 3); // [[2, 3, 4], [0, 1, 2], [10, 20, 30]]
```

```js
juxt(
  (s) => s.length,
  (s) => s.split(" ").join("-")
)("happy coding"); // [[18], ['happy-coding']]
```

Im ersten Beispiel nimmt die `juxt`-Funktion drei Funktionen als Argumente entgegen und gibt eine neue Funktion zurück. Wenn diese neue Funktion mit den Argumenten `1, 2, 3` aufgerufen wird, wendet sie jede der drei Funktionen auf diese Argumente an und gibt ein Array von Arrays zurück, die die Ergebnisse enthalten.

Im zweiten Beispiel nimmt die `juxt`-Funktion zwei Funktionen als Argumente entgegen und gibt eine neue Funktion zurück. Wenn diese neue Funktion mit dem Argument `'happy-coding'` aufgerufen wird, wendet sie jede der beiden Funktionen auf dieses Argument an und gibt ein Array von Arrays zurück, die die Ergebnisse enthalten.
