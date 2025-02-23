# Arrays von aufeinanderfolgenden Elementen finden

Um Arrays von aufeinanderfolgenden Elementen zu finden, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.slice()`, um ein Array zu erstellen, aus dem die ersten `n - 1` Elemente entfernt wurden.
3. Verwenden Sie `Array.prototype.map()` und `Array.prototype.slice()`, um jedes Element zu einem Array von `n` aufeinanderfolgenden Elementen zuzuordnen.

Hier ist eine Beispielfunktion, die diese Schritte implementiert:

```js
const findConsecutive = (arr, n) =>
  arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

Sie können diese Funktion mit einem Array und einer Zahl `n` aufrufen, um alle Arrays von `n` aufeinanderfolgenden Elementen im Array zu finden. Beispiel:

```js
findConsecutive([1, 2, 3, 4, 5], 2);
// [[1, 2], [2, 3], [3, 4], [4, 5]]
```
