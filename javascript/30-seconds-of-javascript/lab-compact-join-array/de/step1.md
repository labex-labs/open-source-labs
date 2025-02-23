# Tipp zur Kompaktierung und Zusammenführung eines Arrays

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist, wie Sie falsche Werte aus einem Array entfernen und die verbleibenden Werte zu einem String kombinieren:

- Verwenden Sie `Array.prototype.filter()`, um falsche Werte wie `false`, `null`, `0`, `""`, `undefined` und `NaN` auszublenden.
- Verwenden Sie `Array.prototype.join()`, um die verbleibenden Werte zu einem String zusammenzufügen.

```js
const compactJoin = (arr, delim = ",") => arr.filter(Boolean).join(delim);
```

Rufen Sie dann die Funktion auf und übergeben Sie ein Array als Argument:

```js
compactJoin(["a", "", "b", "c"]); // 'a,b,c'
```
