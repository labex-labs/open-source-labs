# Wie man überprüft, ob alle Array-Elemente eindeutig sind

Um zu überprüfen, ob alle Elemente in einem Array eindeutig sind, gehen Sie folgenschrittweise vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Erstellen Sie aus den zugeordneten Werten einen neuen `Set`, um nur einzigartige Vorkommen zu behalten.
3. Verwenden Sie `Array.prototype.length` und `Set.prototype.size`, um die Länge der eindeutigen Werte mit dem ursprünglichen Array zu vergleichen.

Hier ist eine Beispiel-Funktion, die diese Schritte implementiert:

```js
const allUnique = (arr) => arr.length === new Set(arr).size;
```

Sie können diese Funktion verwenden, um zu überprüfen, ob ein Array ausschließlich eindeutige Elemente enthält, wie folgt:

```js
allUnique([1, 2, 3, 4]); // true
allUnique([1, 1, 2, 3]); // false
```
