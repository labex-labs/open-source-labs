# Code Übung

Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Anschließend können Sie die Funktion `generateItems` verwenden, um ein Array mit einer bestimmten Anzahl von Elementen zu generieren.

- Rufen Sie `generateItems` mit der gewünschten Anzahl von Elementen und einer Funktion auf, die verwendet werden soll, um die Elemente zu generieren.
- `generateItems` verwendet `Array.from()`, um ein leeres Array der angegebenen Länge zu erstellen und ruft die bereitgestellte Funktion mit dem Index jedes neu erstellten Elements auf.
- Die bereitgestellte Funktion nimmt ein Argument entgegen - den Index jedes Elements.

```js
const generateItems = (n, fn) => Array.from({ length: n }, (_, i) => fn(i));
```

Hier ist ein Beispiel für die Verwendung von `generateItems`, um ein Array von 10 Zufallszahlen zu generieren:

```js
generateItems(10, Math.random);
// [0.21, 0.08, 0.40, 0.96, 0.96, 0.24, 0.19, 0.96, 0.42, 0.70]
```
