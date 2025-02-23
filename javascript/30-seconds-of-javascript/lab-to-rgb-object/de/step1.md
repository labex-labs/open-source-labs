# Umwandlung von RGB in Objekt

Um einen `rgb()`-Farbstring in ein Objekt mit den Werten jeder Farbe umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `String.prototype.match()`, um ein Array von 3 Zeichenketten mit den numerischen Werten zu erhalten.
3. Verwenden Sie `Array.prototype.map()` in Kombination mit `Number`, um sie in ein Array von numerischen Werten umzuwandeln.
4. Verwenden Sie die Array-Destrukturierung, um die Werte in benannte Variablen zu speichern und daraus ein passendes Objekt zu erstellen.

Hier ist der Code, den Sie verwenden können:

```js
const toRGBObject = (rgbStr) => {
  const [red, green, blue] = rgbStr.match(/\d+/g).map(Number);
  return { red, green, blue };
};

toRGBObject("rgb(255, 12, 0)"); // {red: 255, green: 12, blue: 0}
```
