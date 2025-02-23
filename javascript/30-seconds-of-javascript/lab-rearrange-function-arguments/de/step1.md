# Wie man in JavaScript Funktionsargumente neu anordnet

Um in JavaScript Funktionsargumente neu anzuordnen, kann man die `rearg()`-Funktion verwenden. Zunächst erstelle man eine Funktion, die die bereitgestellte Funktion mit ihren Argumenten aufruft, wobei die Argumente gemäß den angegebenen Indizes angeordnet sind. Man kann `Array.prototype.map()` verwenden, um die Argumente basierend auf `indexes` neu zu ordnen. Dann verwendet man den Spread-Operator (`...`), um die transformierten Argumente an `fn` zu übergeben.

Hier ist ein Beispiel, wie man die `rearg()`-Funktion verwendet:

```js
const rearg =
  (fn, indexes) =>
  (...args) =>
    fn(...indexes.map((i) => args[i]));
```

In diesem Beispiel verwenden wir `rearg()`, um eine neue Funktion zu erstellen, die die Argumente einer anderen Funktion neu anordnet.

```js
var rearged = rearg(
  function (a, b, c) {
    return [a, b, c];
  },
  [2, 0, 1]
);
rearged("b", "c", "a"); // ['a', 'b', 'c']
```

In dem obigen Code erstellen wir eine neue Funktion `rearged`, die die Argumente der Funktion `function(a, b, c) { return [a, b, c]; }` neu anordnet. Der `indexes`-Parameter gibt die Reihenfolge an, in der die Argumente neu angeordnet werden sollen. In diesem Fall möchten wir, dass das dritte Argument zuerst kommt, das erste Argument zweitens und das zweite Argument drittens kommt. Wenn wir `rearged('b', 'c', 'a')` aufrufen, wird `['a', 'b', 'c']` zurückgegeben, was das Ergebnis ist, wenn man die ursprüngliche Funktion mit den neu angeordneten Argumenten aufruft.
