# Eine Funktion, die das n-te Argument erhält

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Hier ist, wie Sie eine Funktion erstellen können, die das Argument an Index `n` erhält.

- Verwenden Sie `Array.prototype.slice()`, um das gewünschte Argument an Index `n` zu erhalten.
- Wenn `n` negativ ist, wird das n-te Argument von hinten zurückgegeben.

```js
const nthArg =
  (n) =>
  (...args) =>
    args.slice(n)[0];
```

Hier ist ein Beispiel dafür, wie die `nthArg`-Funktion verwendet wird:

```js
const third = nthArg(2);
console.log(third(1, 2, 3)); // Ausgabe: 3
console.log(third(1, 2)); // Ausgabe: undefined

const last = nthArg(-1);
console.log(last(1, 2, 3, 4, 5)); // Ausgabe: 5
```
