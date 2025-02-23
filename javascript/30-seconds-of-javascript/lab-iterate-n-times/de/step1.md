# Codeübung: N-fache Iteration

Um die Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Nachdem Sie das getan haben, verwenden Sie die folgende Funktion, um einen Callback `n` Mal durchzulaufen:

```js
const times = (n, fn, context = undefined) => {
  let i = 0;
  while (fn.call(context, i) !== false && ++i < n) {}
};
```

Um diese Funktion zu verwenden, rufen Sie `times()` auf und übergeben Sie die folgenden Argumente:

- `n`: Die Anzahl der Male, für die Sie den Callback-Funktion durchlaufen möchten
- `fn`: Die Callback-Funktion, die Sie durchlaufen möchten
- `context` (optional): Der Kontext, den Sie für die Callback-Funktion verwenden möchten (wenn nicht angegeben, wird ein `undefined`-Objekt oder das globale Objekt im nicht-striktem Modus verwendet)

Hier ist ein Beispiel, wie die `times()`-Funktion verwendet werden kann:

```js
var output = "";
times(5, (i) => (output += i));
console.log(output); // 01234
```

Dies wird die Callback-Funktion `i => (output += i)` 5 Mal durchlaufen und das Ergebnis im `output`-Variablen speichern. Das Ergebnis wird dann in der Konsole ausgegeben, was `01234` anzeigen wird.
