# Anweisungen zur Berechnung des Durchschnitts eines abgebildeten Arrays

Um den Durchschnitt eines Arrays zu berechnen, können Sie jedes Element mithilfe der bereitgestellten Funktion auf einen neuen Wert abbilden. Hier sind die Schritte:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.map()`, um jedes Element auf den von `fn` zurückgegebenen Wert abzubilden.
3. Verwenden Sie `Array.prototype.reduce()`, um jeden abgebildeten Wert einem Akkumulator hinzuzufügen, der mit einem Wert von `0` initialisiert wird.
4. Teilen Sie das resultierende Array durch seine Länge, um den Durchschnitt zu erhalten.

Hier ist der Code, den Sie verwenden können:

```js
const averageBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0) / arr.length;
```

Sie können diese Funktion mit den folgenden Beispielen testen:

```js
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (o) => o.n); // 5
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 5
```
