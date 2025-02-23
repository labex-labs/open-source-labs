# Wie man in JavaScript Funktions-Eigenschaftsnamen aus einem Objekt bekommt

Um ein Array von Funktions-Eigenschaftsnamen aus einem Objekt zu erhalten, verwenden Sie die unten bereitgestellte `functions`-Funktion. Diese Funktion kann optional auch ererbte Eigenschaften enthalten.

So verwenden Sie die `functions`-Funktion:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie `Object.keys()`, um über die eigenen Eigenschaften des Objekts zu iterieren.
3. Wenn Sie ererbte Eigenschaften enthalten möchten, legen Sie das Argument `inherited` auf `true` und verwenden Sie `Object.getPrototypeOf()`, um die ererbten Eigenschaften des Objekts zu erhalten.
4. Verwenden Sie `Array.prototype.filter()`, um nur diejenigen Eigenschaften zu behalten, die Funktionen sind.
5. Lassen Sie das zweite Argument, `inherited`, weg, um standardmäßig keine ererbten Eigenschaften zu enthalten.

```js
const functions = (obj, inherited = false) =>
  (inherited
    ? [...Object.keys(obj), ...Object.keys(Object.getPrototypeOf(obj))]
    : Object.keys(obj)
  ).filter((key) => typeof obj[key] === "function");
```

Hier ist ein Beispiel für die Verwendung der `functions`-Funktion:

```js
function Foo() {
  this.a = () => 1;
  this.b = () => 2;
}
Foo.prototype.c = () => 3;
functions(new Foo()); // ['a', 'b']
functions(new Foo(), true); // ['a', 'b', 'c']
```
