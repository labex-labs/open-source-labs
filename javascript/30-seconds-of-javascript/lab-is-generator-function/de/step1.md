# Überprüfen, ob ein Wert eine Generatorfunktion ist

Um zu überprüfen, ob ein Wert eine Generatorfunktion ist, können Sie die `isGeneratorFunction`-Funktion verwenden. Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

So funktioniert die `isGeneratorFunction`-Funktion:

- Sie überprüft, ob das angegebene Argument eine Generatorfunktion ist, indem sie `Object.prototype.toString()` und `Function.prototype.call()` verwendet.
- Wenn das Ergebnis der Prüfung `'[object GeneratorFunction]'` ist, ist der Wert eine Generatorfunktion.

Hier ist der Code für die `isGeneratorFunction`-Funktion:

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

Und hier sind einige Beispiele für die Verwendung:

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
