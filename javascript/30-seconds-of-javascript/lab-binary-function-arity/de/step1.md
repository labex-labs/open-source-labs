# Funktion, die bis zu zwei Argumente akzeptiert

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die `binary`-Funktion wird erstellt, um bis zu zwei Argumente akzeptieren zu können, während alle zusätzlichen ignoriert werden.

Die bereitgestellte `fn`-Funktion wird mit den ersten zwei gegebenen Argumenten aufgerufen.

Hier ist der Code:

```js
const binary = (fn) => (a, b) => fn(a, b);
```

Und hier ist ein Beispiel für die Verwendung:

```js
["2", "1", "0"].map(binary(Math.max)); // [2, 1, 2]
```
