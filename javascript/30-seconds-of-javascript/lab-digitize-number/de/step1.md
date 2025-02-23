# Wie man eine Zahl in Ziffern zerlegt

Um eine Zahl in JavaScript in Ziffern zu zerlegen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Math.abs()`, um das Vorzeichen der Zahl zu entfernen.
3. Konvertieren Sie die Zahl in einen String und verwenden Sie den Spread-Operator (`...`), um ein Array von Ziffern zu erstellen.
4. Verwenden Sie `Array.prototype.map()` und `parseInt()`, um jede Ziffer in eine Ganzzahl umzuwandeln.

Hier ist der Code für die `digitize`-Funktion:

```js
const digitize = (n) => [...`${Math.abs(n)}`].map((i) => parseInt(i));
```

Beispielverwendung:

```js
digitize(123); // [1, 2, 3]
digitize(-123); // [1, 2, 3]
```
