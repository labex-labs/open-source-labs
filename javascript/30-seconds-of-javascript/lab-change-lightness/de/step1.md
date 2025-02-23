# Wie man die Helligkeit einer HSL-Farbe ändert

Um den Helligkeitswert eines `hsl()`-Farbstrohstrings zu ändern, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Verwenden Sie `String.prototype.match()`, um ein Array von drei Strings mit den numerischen Werten aus dem `hsl()`-String zu erhalten.

3. Verwenden Sie `Array.prototype.map()` in Kombination mit `Number`, um die Strings in ein Array von numerischen Werten zu konvertieren.

4. Stellen Sie sicher, dass der Helligkeitswert im gültigen Bereich (zwischen `0` und `100`) liegt, indem Sie `Math.max()` und `Math.min()` verwenden.

5. Verwenden Sie eine Template-Literal, um einen neuen `hsl()`-String mit dem aktualisierten Helligkeitswert zu erstellen.

Hier ist ein Beispielcodeausschnitt, der diese Schritte implementiert:

```js
const changeLightness = (delta, hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);

  const newLightness = Math.max(
    0,
    Math.min(100, lightness + parseFloat(delta))
  );

  return `hsl(${hue}, ${saturation}%, ${newLightness}%)`;
};
```

Sie können dann die `changeLightness()`-Funktion mit einem Delta-Wert und einem `hsl()`-String aufrufen, um einen neuen `hsl()`-String mit dem aktualisierten Helligkeitswert zu erhalten. Beispielsweise:

```js
changeLightness(10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 60%)'
changeLightness(-10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 40%)'
```
