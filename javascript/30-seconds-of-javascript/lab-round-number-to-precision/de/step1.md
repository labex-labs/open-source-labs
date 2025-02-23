# So runden Sie eine Zahl in JavaScript auf eine bestimmte Genauigkeit:

```
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`);
```

- Verwenden Sie `Math.round()` und Template-Literale, um die Zahl auf die angegebene Anzahl von Dezimalstellen zu runden.
- Wenn Sie auf eine ganze Zahl runden möchten, lassen Sie das zweite Argument `decimals` weg.
- Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
- Beispielsweise wird `round(1.005, 2)` `1.01` zurückgeben.
