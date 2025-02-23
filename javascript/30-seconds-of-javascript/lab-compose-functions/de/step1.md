# Wie man Funktionen in JavaScript zusammensetzt

Um zu beginnen, mit der Programmierung mit Funktionskomposition in JavaScript zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist ein Beispiel dafür, wie man eine rechts-links-Funktionskomposition in JavaScript durchführt:

1. Verwenden Sie `Array.prototype.reduce()`, um eine rechts-links-Funktionskomposition durchzuführen.
2. Die letzte (rechtsmöglichste) Funktion kann einen oder mehrere Argumente akzeptieren; die verbleibenden Funktionen müssen einstellige Funktionen sein.
3. Definieren Sie die `compose`-Funktion, die beliebig viele Funktionen als Argumente entgegennimmt und eine neue Funktion zurückgibt, die diese zusammensetzt.
4. Rufen Sie die `compose`-Funktion mit den gewünschten Funktionen in der gewünschten Reihenfolge auf.
5. Rufen Sie die neue zusammengesetzte Funktion mit allen erforderlichen Argumenten auf.

```js
const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args))
  );
```

Nehmen wir beispielsweise an, dass wir zwei Funktionen haben:

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
```

Wir können diese Funktionen mit `compose` zusammensetzen:

```js
const multiplyAndAdd5 = compose(add5, multiply);
```

Jetzt können wir `multiplyAndAdd5` mit den gewünschten Argumenten aufrufen:

```js
multiplyAndAdd5(5, 2); // 15
```
