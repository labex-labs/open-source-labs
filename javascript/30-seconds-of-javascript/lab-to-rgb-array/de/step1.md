# Umwandeln einer RGB-Zeichenfolge in ein Array

Um eine `rgb()`-Farbstirng in ein Array von Werten umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `String.prototype.match()`, um ein Array von 3 Zeichenfolgen mit den numerischen Werten zu erhalten.
3. Verwenden Sie `Array.prototype.map()` in Kombination mit `Number`, um sie in ein Array numerischer Werte umzuwandeln.

Hier ist der Code, den Sie verwenden können:

```js
const toRGBArray = (rgbStr) => rgbStr.match(/\d+/g).map(Number);
```

Um die Funktion zu testen, rufen Sie sie mit einer `rgb()`-Farbstirng als Argument auf, wie folgt:

```js
toRGBArray("rgb(255, 12, 0)"); // [255, 12, 0]
```
