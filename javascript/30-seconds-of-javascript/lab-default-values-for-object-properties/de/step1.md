# Wie man Standardwerte für Objekteigenschaften zuweist

Um Standardwerte für alle Eigenschaften in einem Objekt zuzuweisen, die `undefined` sind, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Object.assign()`, um ein neues leeres Objekt zu erstellen und das ursprüngliche zu kopieren, um die Schlüsselreihenfolge beizubehalten.
3. Verwenden Sie `Array.prototype.reverse()` und den Spread-Operator (`...`), um die Standardwerte von links nach rechts zu kombinieren.
4. Am Ende verwenden Sie `obj` erneut, um Eigenschaften zu überschreiben, die ursprünglich einen Wert hatten.

Hier ist ein Beispielcodeausschnitt:

```js
const defaults = (obj, ...defs) =>
  Object.assign({}, obj, ...defs.reverse(), obj);

defaults({ a: 1 }, { b: 2 }, { b: 6 }, { a: 3 }); // { a: 1, b: 2 }
```

Dieser Codeausschnitt wird ein Objekt zurückgeben, das Standardwerte für alle Eigenschaften hat, die im ursprünglichen Objekt `undefined` waren.
