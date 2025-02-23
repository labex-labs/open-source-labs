# Anweisungen für den Zyklusgenerator

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Anschließend erstellen Sie einen Generator, der unendlich über das gegebene Array iteriert. Hier sind die Schritte:

1. Verwenden Sie eine nicht endende `while`-Schleife, die jedes Mal, wenn `Generator.prototype.next()` aufgerufen wird, einen Wert `yield` gibt.
2. Verwenden Sie den Modulo-Operator (`%`) mit `Array.prototype.length`, um den Index des nächsten Werts zu erhalten und den Zähler nach jeder `yield`-Anweisung zu erhöhen.

Hier ist ein Beispiel für die `cycleGenerator`-Funktion:

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

Sie können die Funktion dann wie folgt verwenden:

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

Mit diesen Anweisungen können Sie einen Zyklusgenerator erstellen, der unendlich über jedes Array iteriert.
