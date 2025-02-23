# Wie man Werte aus einem Array basierend auf einer gegebenen Funktion extrahiert

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die Funktion `pullBy` verändert das ursprüngliche Array, indem sie die angegebenen Werte basierend auf einer gegebenen Iterationsfunktion herausfiltert. So funktioniert es:

1. Überprüfen, ob das letzte übergebene Argument eine Funktion ist.
2. Verwenden Sie `Array.prototype.map()`, um die Iterationsfunktion `fn` auf alle Arrayelemente anzuwenden.
3. Verwenden Sie `Array.prototype.filter()` und `Array.prototype.includes()`, um die nicht benötigten Werte herauszuziehen.
4. Setzen Sie `Array.prototype.length`, um die Länge des übergebenen Arrays auf `0` zurückzusetzen.
5. Verwenden Sie `Array.prototype.push()`, um es nur mit den extrahierten Werten neu zu befüllen.

Hier ist der Code:

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val)
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

Und hier ist ein Beispiel, wie man es verwenden kann:

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

Beachten Sie, dass wir in diesem Beispiel alle Elemente mit einer `x`-Eigenschaft von `1` oder `3` herausziehen. Das resultierende `myArray` wird nur das Element mit einer `x`-Eigenschaft von `2` enthalten.
