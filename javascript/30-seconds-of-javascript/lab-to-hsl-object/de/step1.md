# Umwandlung von HSL in Objekt

Um einen `hsl()`-Farbstring in ein Objekt mit den numerischen Werten jeder Farbe umzuwandeln, folgen Sie diesen Schritten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Verwenden Sie `String.prototype.match()`, um ein Array von 3 Strings mit den numerischen Werten zu erhalten.
- Konvertieren Sie die Strings in ein Array von numerischen Werten, indem Sie `Array.prototype.map()` in Kombination mit `Number` verwenden.
- Speichern Sie die Werte in benannten Variablen, indem Sie Array-Destrukturierung verwenden.
- Erstellen Sie aus den benannten Variablen ein passendes Objekt.

```js
const toHSLObject = (hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);
  return { hue, saturation, lightness };
};
```

Beispielverwendung:

```js
toHSLObject("hsl(50, 10%, 10%)"); // { hue: 50, saturation: 10, lightness: 10 }
```
