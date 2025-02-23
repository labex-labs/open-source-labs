# RGB zu Hex-Converter

Um RGB-Werte in einen hexadezimalen Farbcode umzuwandeln:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Verwenden Sie die folgende Funktion:

```js
const RGBToHex = (r, g, b) =>
  ((r << 16) + (g << 8) + b).toString(16).padStart(6, "0");
```

3. Rufen Sie die Funktion mit den RGB-Werten als Argumenten auf, um einen 6-stelligen hexadezimalen Wert zu erhalten.

Beispiel:

```js
RGBToHex(255, 165, 1); // 'ffa501'
```
