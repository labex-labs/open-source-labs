# Wie man eine Prädikatfunktion in JavaScript negiert

Um eine Prädikatfunktion in JavaScript zu negieren, kannst du den `!`-Operator verwenden. Dazu kannst du eine Higher-Order-Funktion namens `negate` erstellen, die eine Prädikatfunktion annimmt und den `!`-Operator mit ihren Argumenten darauf anwendet. Hier ist ein Beispiel dafür, wie man `negate` implementiert:

```js
const negate =
  (func) =>
  (...args) =>
    !func(...args);
```

Dann kannst du `negate` verwenden, um jede Prädikatfunktion zu negieren. Hier ist ein Beispiel dafür, wie man `negate` verwendet, um gerade Zahlen aus einem Array zu filtern:

```js
const isEven = (n) => n % 2 === 0;
const isOdd = negate(isEven);

[1, 2, 3, 4, 5, 6].filter(isOdd); // [ 1, 3, 5 ]
```

In diesem Beispiel ist `isEven` eine Prädikatfunktion, die überprüft, ob eine Zahl gerade ist. Dann verwenden wir `negate`, um eine neue Prädikatfunktion namens `isOdd` zu erstellen, die überprüft, ob eine Zahl ungerade ist, indem sie `isEven` negiert. Schließlich verwenden wir `isOdd` mit der `filter`-Methode, um gerade Zahlen aus dem Array zu filtern.
