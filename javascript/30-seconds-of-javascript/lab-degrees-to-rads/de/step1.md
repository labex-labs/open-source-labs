# Umwandlung von Grad in Bogenmaß

Um einen Winkel von Grad in Bogenmaß umzurechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH.
2. Geben Sie `node` ein, um zu beginnen zu programmieren.
3. Verwenden Sie die Formel für die Umrechnung von Grad in Bogenmaß zusammen mit `Math.PI`.
4. Wenden Sie die Formel auf den Winkel in Grad an, um den Winkel in Bogenmaß zu erhalten.

Hier ist die Formel in JavaScript:

```js
const degreesToRads = (deg) => (deg * Math.PI) / 180.0;
```

Beispielsweise können Sie die `degreesToRads`-Funktion wie folgt verwenden, um 90 Grad in Bogenmaß umzurechnen:

```js
degreesToRads(90.0); // ~1.5708
```
