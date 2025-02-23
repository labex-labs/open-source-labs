# RGB-HSL-Umwandlung

Um ein RGB-Farbtupel in das HSL-Format umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH, um mit der Programmierung zu beginnen.
2. Tippen Sie `node` und drücken Sie die Eingabetaste.
3. Verwenden Sie die [RGB-HSL-Umrechnungsformel](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/), um in das entsprechende Format umzuwandeln.
4. Stellen Sie sicher, dass alle Eingabeparameter im Bereich von [0, 255] liegen.
5. Die resultierenden Werte sollten im Bereich von H: [0, 360], S: [0, 100], L: [0, 100] liegen.

Hier ist ein Beispiel für die RGBToHSL-Funktion in JavaScript:

```js
const RGBToHSL = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const l = Math.max(r, g, b);
  const s = l - Math.min(r, g, b);
  const h = s
    ? l === r
      ? (g - b) / s
      : l === g
        ? 2 + (b - r) / s
        : 4 + (r - g) / s
    : 0;
  return [
    60 * h < 0 ? 60 * h + 360 : 60 * h,
    100 * (s ? (l <= 0.5 ? s / (2 * l - s) : s / (2 - (2 * l - s))) : 0),
    (100 * (2 * l - s)) / 2
  ];
};
```

Hier ist ein Beispiel dafür, wie die RGBToHSL-Funktion verwendet werden kann:

```js
RGBToHSL(45, 23, 11); // [21.17647, 60.71428, 10.98039]
```
