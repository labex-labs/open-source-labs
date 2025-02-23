# Wie man ein Array in ein Objekt gruppiert

Um ein Array in ein Objekt zu gruppieren, folge diesen Schritten:

1. Öffne das Terminal oder SSH und tippe `node`, um zu beginnen, zu programmieren.
2. Verwende die `Array.prototype.reduce()`-Methode, um ein Objekt aus den beiden Arrays zu erstellen.
3. Gib ein Array von gültigen Eigenschaftsbezeichnern und ein Array von Werten an.
4. Wenn die Länge des Eigenschaftsarrays länger als das Wertesarray ist, werden die verbleibenden Schlüssel auf `undefined` gesetzt.
5. Wenn die Länge des Wertesarrays länger als das Eigenschaftsarray ist, werden die verbleibenden Werte ignoriert.

Hier ist ein Beispielcodeausschnitt, der zeigt, wie man ein Array in ein Objekt gruppiert:

```js
const zipObject = (props, values) =>
  props.reduce((obj, prop, index) => ((obj[prop] = values[index]), obj), {});

zipObject(["a", "b", "c"], [1, 2]); // {a: 1, b: 2, c: undefined}
zipObject(["a", "b"], [1, 2, 3]); // {a: 1, b: 2}
```
