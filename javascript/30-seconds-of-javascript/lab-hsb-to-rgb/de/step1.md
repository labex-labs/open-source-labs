# Umwandlung von HSB in RGB

Um ein HSB-Farb-Tupel in das RGB-Format umzuwandeln, folgen Sie diesen Schritten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
- Verwenden Sie die [Formel zur Umwandlung von HSB in RGB](https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB), um in das entsprechende Format umzuwandeln.
- Die Eingabeparameter sollten im Bereich H: [0, 360], S: [0, 100], B: [0, 100] liegen.
- Alle Ausgabewerte sollten im Bereich [0, 255] liegen.

Hier ist der Code, den Sie verwenden können, um HSB in RGB umzuwandeln:

```js
const HSBToRGB = (h, s, b) => {
  s /= 100;
  b /= 100;
  const k = (n) => (n + h / 60) % 6;
  const f = (n) => b * (1 - s * Math.max(0, Math.min(k(n), 4 - k(n), 1)));
  return [255 * f(5), 255 * f(3), 255 * f(1)];
};
```

Beispielsweise können Sie den folgenden Code verwenden, um das HSB-Farb-Tupel (18, 81, 99) in das RGB-Format umzuwandeln:

```js
HSBToRGB(18, 81, 99); // [252.45, 109.31084999999996, 47.965499999999984]
```
