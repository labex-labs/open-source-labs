# Umkehrung der Funktionskomposition

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist, wie man eine Funktionskomposition von links nach rechts durchführt:

- Verwenden Sie die `Array.prototype.reduce()`-Methode, um eine Funktionskomposition von links nach rechts durchzuführen.
- Die erste (am linkesten) Funktion kann einen oder mehrere Argumente akzeptieren, während die verbleibenden Funktionen unär sein müssen.

```js
const composeRight = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args))
  );
```

Beispiel:

```js
const add = (x, y) => x + y;
const square = (x) => x * x;
const addAndSquare = composeRight(add, square);
addAndSquare(1, 2); // 9
```
