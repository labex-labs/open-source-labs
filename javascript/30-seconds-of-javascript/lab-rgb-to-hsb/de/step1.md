# RGB zu HSB Konvertierung

Um ein RGB-Farb-Tupel in das HSB-Format umzuwandeln, können Sie die folgenden Schritte ausführen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie die [RGB zu HSB-Konversionsformel](https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB), um das RGB-Farb-Tupel in das entsprechende HSB-Format umzuwandeln.
3. Der Bereich der Eingabeparameter ist [0, 255], während die resultierenden Werte einen Bereich haben von:

- H: [0, 360]
- S: [0, 100]
- B: [0, 100]

Hier ist die Funktion in JavaScript:

```js
const RGBToHSB = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const v = Math.max(r, g, b),
    n = v - Math.min(r, g, b);
  const h =
    n === 0
      ? 0
      : n && v === r
        ? (g - b) / n
        : v === g
          ? 2 + (b - r) / n
          : 4 + (r - g) / n;
  return [60 * (h < 0 ? h + 6 : h), v && (n / v) * 100, v * 100];
};
```

Sie können die Funktion wie folgt aufrufen:

```js
RGBToHSB(252, 111, 48);
// [18.529411764705856, 80.95238095238095, 98.82352941176471]
```
