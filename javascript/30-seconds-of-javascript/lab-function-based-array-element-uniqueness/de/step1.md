# Überprüfen, ob alle Elemente eines Arrays mit einer Funktion eindeutig sind

Um zu überprüfen, ob alle Elemente eines Arrays eindeutig sind, basierend auf einer bereitgestellten Zuordnungsfunktion, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die `Array.prototype.map()`-Methode, um die bereitgestellte Funktion `fn` auf alle Elemente im `arr`-Array anzuwenden.
3. Erstellen Sie aus den zugeordneten Werten einen neuen `Set`, um nur einzigartige Vorkommen zu behalten.
4. Vergleichen Sie die Länge der einzigartigen zugeordneten Werte mit der Länge des ursprünglichen Arrays, indem Sie die `Array.prototype.length`- und `Set.prototype.size`-Methoden verwenden.

Hier ist der Code:

```js
const allUniqueBy = (arr, fn) => arr.length === new Set(arr.map(fn)).size;
```

Sie können die `allUniqueBy()`-Funktion verwenden, um zu überprüfen, ob alle Elemente eines Arrays eindeutig sind. Beispielsweise:

```js
allUniqueBy([1.2, 2.4, 2.9], Math.round); // true
allUniqueBy([1.2, 2.3, 2.4], Math.round); // false
```
