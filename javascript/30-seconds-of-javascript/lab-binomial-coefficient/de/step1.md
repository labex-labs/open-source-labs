# Binomialkoeffizientberechnung

Um die Anzahl der Möglichkeiten zu berechnen, `k` Elemente aus `n` Elementen ohne Wiederholung und ohne Berücksichtigung der Reihenfolge auszuwählen, können Sie die folgende JavaScript-Funktion verwenden:

```js
const binomialCoefficient = (n, k) => {
  if (Number.isNaN(n) || Number.isNaN(k)) return NaN;
  if (k < 0 || k > n) return 0;
  if (k === 0 || k === n) return 1;
  if (k === 1 || k === n - 1) return n;
  if (n - k < k) k = n - k;
  let res = n;
  for (let j = 2; j <= k; j++) res *= (n - j + 1) / j;
  return Math.round(res);
};
```

Um die Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Rufen Sie dann die Funktion mit den gewünschten Werten auf. Beispielsweise:

```js
binomialCoefficient(8, 2); // 28
```

Um sicherzustellen, dass die Funktion korrekt funktioniert, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `Number.isNaN()`, um zu überprüfen, ob einer der beiden Werte `NaN` ist.
2. Überprüfen Sie, ob `k` kleiner als `0`, größer als oder gleich `n`, gleich `1` oder `n - 1` ist und geben Sie das entsprechende Ergebnis zurück.
3. Überprüfen Sie, ob `n - k` kleiner als `k` ist und tauschen Sie deren Werte entsprechend.
4. Schleifen Sie von `2` bis `k` und berechnen Sie den Binomialkoeffizienten.
5. Verwenden Sie `Math.round()`, um Rundungsfehler bei der Berechnung zu berücksichtigen.
