# Erstellen einer Funktion mit einem angegebenen Kontext

Um eine Funktion mit einem angegebenen Kontext zu erstellen, verwenden Sie die `bind`-Funktion. Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein.

Die `bind`-Funktion erstellt eine neue Funktion, die die ursprüngliche Funktion mit einem angegebenen Kontext aufruft. Optionaler kann sie auch alle zusätzlichen übergebenen Parameter an die Argumente anhängen.

Um `bind` zu verwenden, übergeben Sie die ursprüngliche Funktion (`fn`) und den gewünschten Kontext (`context`). Sie können auch alle zusätzlichen Parameter übergeben, die an die Funktion gebunden werden sollen (`...boundArgs`).

Die `bind`-Funktion gibt eine neue Funktion zurück, die `Function.prototype.apply()` verwendet, um den angegebenen `Kontext` auf `fn` anzuwenden. Sie verwendet auch den Spread-Operator (`...`), um alle zusätzlichen übergebenen Parameter an die Argumente anzuhängen.

Hier ist ein Beispiel für die Verwendung von `bind`:

```js
const bind =
  (fn, context, ...boundArgs) =>
  (...args) =>
    fn.apply(context, [...boundArgs, ...args]);

function greet(greeting, punctuation) {
  return greeting + " " + this.user + punctuation;
}

const freddy = { user: "fred" };
const freddyBound = bind(greet, freddy);
console.log(freddyBound("hi", "!")); // 'hi fred!'
```

In diesem Beispiel definieren wir eine `greet`-Funktion, die zwei Parameter (`greeting` und `punctuation`) nimmt und einen String zurückgibt, der die `greeting`, die `user`-Eigenschaft des aktuellen Kontexts (`this`) und die `punctuation` zusammenfügt.

Wir erstellen dann ein neues Objekt (`freddy`), das eine `user`-Eigenschaft mit dem Wert `'fred'` hat.

Schließlich erstellen wir eine neue Funktion (`freddyBound`) mit `bind`, wobei wir die `greet`-Funktion und das `freddy`-Objekt als gewünschten Kontext übergeben. Anschließend können wir `freddyBound` mit zwei zusätzlichen Parametern (`'hi'` und `'!'`) aufrufen, die zusammen mit dem gebundenen `freddy`-Kontext an die ursprüngliche `greet`-Funktion übergeben werden. Das resultierende Ausgabe ist `'hi fred!'`.
