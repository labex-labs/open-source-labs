# Wie man die Vereinigung zweier Arrays in JavaScript findet

Um die Vereinigung zweier Arrays in JavaScript zu finden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Die Vereinigung zweier Arrays liefert jedes Element, das in einem der beiden Arrays mindestens einmal vorhanden ist.

3. Um die Vereinigung zweier Arrays zu erhalten, erstellen Sie eine `Set` mit allen Werten von `a` und `b` und konvertieren Sie sie mit der `Array.from()`-Methode in ein Array.

Hier ist ein Beispiel, wie dies implementiert werden kann:

```js
const union = (a, b) => Array.from(new Set([...a, ...b]));

console.log(union([1, 2, 3], [4, 3, 2])); // Ausgabe: [1, 2, 3, 4]
```

Im obigen Beispiel nimmt die `union()`-Funktion zwei Arrays, `[1, 2, 3]` und `[4, 3, 2]`, als Argumente entgegen und gibt die Vereinigung der beiden Arrays als Array `[1, 2, 3, 4]` zurück.
