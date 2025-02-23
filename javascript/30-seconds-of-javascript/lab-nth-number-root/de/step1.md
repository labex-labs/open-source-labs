# Wie man die n-te Wurzel einer Zahl berechnet

Um die n-te Wurzel einer Zahl zu berechnen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codierung zu beginnen.
2. Verwenden Sie die Formel `Math.pow(x, 1/n)`, um `x` hoch `1/n` zu berechnen.
3. Das Ergebnis dieser Berechnung ist gleich der n-ten Wurzel von `x`.

Hier ist ein Beispiel-Codeausschnitt:

```js
const nthRoot = (x, n) => Math.pow(x, 1 / n);
nthRoot(32, 5); // Ausgabe: 2
```

Dieser Code berechnet die fünfte Wurzel von 32 (wobei n gleich 5 ist) und gibt die Ausgabe als 2 zurück.
