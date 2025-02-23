# Hex zu RGB Konvertierung

Um einen hexadezimalen Farbcode (mit oder ohne `#`-Prefix) in einen RGB-String umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den bitweisen Rechtsshift-Operator und maskieren Sie Bits mit dem `&` (und)-Operator.
3. Wenn der Farbcode 3-stellig ist, konvertieren Sie ihn zunächst in die 6-stellige Version.
4. Wenn ein Alphawert neben dem 6-stelligen Hex-Code angegeben ist, geben Sie einen `rgba()`-String zurück.

Hier ist der JavaScript-Code für die Konvertierung:

```js
const hexToRGB = (hex) => {
  let alpha = false,
    h = hex.slice(hex.startsWith("#") ? 1 : 0);
  if (h.length === 3) h = [...h].map((x) => x + x).join("");
  else if (h.length === 8) alpha = true;
  h = parseInt(h, 16);
  return (
    "rgb" +
    (alpha ? "a" : "") +
    "(" +
    (h >>> (alpha ? 24 : 16)) +
    ", " +
    ((h & (alpha ? 0x00ff0000 : 0x00ff00)) >>> (alpha ? 16 : 8)) +
    ", " +
    ((h & (alpha ? 0x0000ff00 : 0x0000ff)) >>> (alpha ? 8 : 0)) +
    (alpha ? `, ${h & 0x000000ff}` : "") +
    ")"
  );
};
```

Sie können die `hexToRGB`-Funktion mit den folgenden Beispielen verwenden:

```js
hexToRGB("#27ae60ff"); // 'rgba(39, 174, 96, 255)'
hexToRGB("27ae60"); // 'rgb(39, 174, 96)'
hexToRGB("#fff"); // 'rgb(255, 255, 255)'
```
