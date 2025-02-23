# Funktionargumente transformieren

Um Funktionargumente zu transformieren, verwenden Sie die `overArgs`-Funktion, die eine neue Funktion erstellt, die die bereitgestellte Funktion mit transformierten Argumenten aufruft.

- Um die Argumente zu transformieren, verwenden Sie `Array.prototype.map()` in Kombination mit dem Spread-Operator (`...`) und übergeben Sie die transformierten Argumente an `fn`.

```js
const overArgs =
  (fn, transforms) =>
  (...args) =>
    fn(...args.map((val, i) => transforms[i](val)));
```

- Um die `overArgs`-Funktion zu testen, erstellen Sie eine Beispiel-Funktion und ein Array von Transformationen und rufen Sie dann die neue Funktion mit Argumenten auf.

```js
const square = (n) => n * n;
const double = (n) => n * 2;

const fn = overArgs((x, y) => [x, y], [square, double]);
fn(9, 3); // [81, 6]
```

Um mit der Code-Praxis zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
