# Funktion zum Binden von Objektmethoden

Um eine Funktion zu erstellen, die eine Objektmethode an ihren Kontext bindet und optional zusätzliche Parameter anhängt, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Definieren Sie eine Funktion, die drei Parameter annimmt: den Objektkontext, den Methodenschlüssel und alle zusätzlichen Argumente, die angehängt werden sollen.
3. Die Funktion sollte eine neue Funktion zurückgeben, die `Function.prototype.apply()` verwendet, um die Methode an den Objektkontext zu binden.
4. Verwenden Sie den Spread-Operator (`...`), um alle zusätzlichen übergebenen Parameter den Argumenten anzuhängen.
5. Hier ist eine Beispielimplementierung:

```js
const bindKey =
  (context, fn, ...boundArgs) =>
  (...args) =>
    context[fn].apply(context, [...boundArgs, ...args]);
```

6. Um die Funktion zu testen, erstellen Sie ein Objekt mit einer Methode und binden Sie es mit `bindKey()`. Rufen Sie dann die gebundene Methode mit einigen Argumenten auf.

```js
const freddy = {
  user: "fred",
  greet: function (greeting, punctuation) {
    return greeting + " " + this.user + punctuation;
  }
};
const freddyBound = bindKey(freddy, "greet");
console.log(freddyBound("hi", "!")); // 'hi fred!'
```
