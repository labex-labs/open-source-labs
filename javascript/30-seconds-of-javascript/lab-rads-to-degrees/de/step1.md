# Umwandeln von Radiant in Grad

Um einen Winkel von Radiant in Grad umzurechnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die folgende Formel: `degrees = radians * (180 / Math.PI)`
3. Ersetzen Sie in der Formel `radians` durch den Wert, den Sie umwandeln möchten.
4. Das Ergebnis wird in Grad vorliegen.

Hier ist ein Beispiel:

```js
const radsToDegrees = (rad) => (rad * 180.0) / Math.PI;
radsToDegrees(Math.PI / 2); // 90
```

Dies wird `π/2` Radiant in `90` Grad umwandeln.
