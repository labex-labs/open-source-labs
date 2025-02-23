# Funktion, die Argumente anhängt

Um eine Funktion zu erstellen, die Argumente an die von ihr empfangenen anhängt, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um die Code-Praxis zu starten.
2. Verwenden Sie den Spread-Operator (`...`), um `Partials` zur Liste der Argumente von `fn` hinzuzufügen.
3. Verwenden Sie den folgenden Code, um die Funktion zu erstellen:

```js
const partialRight =
  (fn, ...partials) =>
  (...args) =>
    fn(...args, ...partials);
```

4. Testen Sie die Funktion mit einem Beispiel, wie z. B.:

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetJohn = partialRight(greet, "John");
greetJohn("Hello"); // 'Hello John!'
```
