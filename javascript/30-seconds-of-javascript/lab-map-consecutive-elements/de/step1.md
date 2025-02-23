# Funktion zum Abbilden aufeinanderfolgender Elemente in einem Array

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Diese Funktion bildet jedes Block von `n` aufeinanderfolgenden Elementen in einem Array mit der angegebenen Funktion `fn` ab. Folgen Sie diesen Schritten:

- Verwenden Sie `Array.prototype.slice()`, um ein neues Array `arr` zu erhalten, von dem die ersten `n` Elemente entfernt wurden.
- Verwenden Sie `Array.prototype.map()` und `Array.prototype.slice()`, um `fn` auf jeden Block von `n` aufeinanderfolgenden Elementen in `arr` anzuwenden.

Hier ist der Code:

```js
const mapConsecutive = (arr, n, fn) =>
  arr.slice(n - 1).map((v, i) => fn(arr.slice(i, i + n)));
```

Beispielsweise können Sie `mapConsecutive()` verwenden, um jeden Block von 3 aufeinanderfolgenden Elementen in einem Array von Zahlen abzubilden und sie mit Bindestrichen zu verbinden:

```js
mapConsecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, (x) => x.join("-"));
// ['1-2-3', '2-3-4', '3-4-5', '4-5-6', '5-6-7', '6-7-8', '7-8-9', '8-9-10'];
```
