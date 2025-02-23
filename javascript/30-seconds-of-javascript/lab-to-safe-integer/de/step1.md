# Ein Wert in einen sicheren ganzzahligen Wert umwandeln

Um einen Wert in einen sicheren ganzzahligen Wert umzuwandeln, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Math.max()` und `Math.min()`, um den nächsten sicheren Wert zu finden.
3. Verwenden Sie `Math.round()`, um den Wert in einen ganzzahligen Wert umzuwandeln.

Hier ist ein Beispielcodeausschnitt, der zeigt, wie ein Wert in einen sicheren ganzzahligen Wert umgewandelt wird:

```js
const toSafeInteger = (num) =>
  Math.round(
    Math.max(Math.min(num, Number.MAX_SAFE_INTEGER), Number.MIN_SAFE_INTEGER)
  );
```

Sie können diese Funktion mit der folgenden Eingabe testen:

```js
toSafeInteger("3.2"); // 3
toSafeInteger(Infinity); // 9007199254740991
```
