# HSL in RGB mit JavaScript umwandeln

Um ein Farbtupel im HSL-Format in RGB umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie die [Formel zur Umrechnung von HSL in RGB](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB), um das Farbtupel in das entsprechende Format umzuwandeln.
3. Stellen Sie sicher, dass die Eingabeparameter im folgenden Bereich liegen: H: [0, 360], S: [0, 100], L: [0, 100].
4. Die Ausgabewerte sollten im Bereich [0, 255] liegen.

Hier ist der JavaScript-Code für die Formel zur Umrechnung von HSL in RGB:

```js
const HSLToRGB = (h, s, l) => {
  s /= 100;
  l /= 100;
  const k = (n) => (n + h / 30) % 12;
  const a = s * Math.min(l, 1 - l);
  const f = (n) =>
    l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
  return [255 * f(0), 255 * f(8), 255 * f(4)];
};
```

Um die Funktion zu verwenden, geben Sie die H-, S- und L-Werte als Argumente an:

```js
HSLToRGB(13, 100, 11); // [56.1, 12.155, 0]
```
