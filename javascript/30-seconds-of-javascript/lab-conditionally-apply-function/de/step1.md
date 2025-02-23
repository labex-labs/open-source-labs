# Verwenden der `when`-Funktion, um eine Bedingung anzuwenden

Um eine Funktion anzuwenden, wenn eine bestimmte Bedingung erfüllt ist, verwenden Sie die `when`-Funktion. Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein.

Die `when`-Funktion gibt eine neue Funktion zurück, die ein Argument annimmt und einen Callback ausführt, wenn das Argument wahr ist, oder das Argument zurückgibt, wenn es falsch ist. Die Funktion erwartet einen einzelnen Wert, `x`, und gibt den entsprechenden Wert basierend auf dem `pred`-Parameter zurück.

Hier ist eine Beispielimplementierung der `when`-Funktion:

```js
const when = (pred, whenTrue) => (x) => (pred(x) ? whenTrue(x) : x);
```

Sie können die `when`-Funktion verwenden, um eine neue Funktion zu erstellen, die gerade Zahlen verdoppelt:

```js
const doubleEvenNumbers = when(
  (x) => x % 2 === 0,
  (x) => x * 2
);
doubleEvenNumbers(2); // 4
doubleEvenNumbers(1); // 1
```
