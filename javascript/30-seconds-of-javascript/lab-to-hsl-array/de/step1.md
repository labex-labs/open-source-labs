# HSL in ein Array umwandeln

Um einen `hsl()`-Farbenstring in ein Array von Werten umzuwandeln, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `String.prototype.match()`, um ein Array von 3 Strings mit den numerischen Werten zu erhalten.
3. Verwenden Sie `Array.prototype.map()` in Kombination mit `Number`, um sie in ein Array von numerischen Werten umzuwandeln.

Hier ist der Code, um einen `hsl()`-Farbenstring in ein Array von numerischen Werten umzuwandeln:

```js
const toHSLArray = (hslStr) => hslStr.match(/\d+/g).map(Number);
```

Beispielverwendung:

```js
toHSLArray("hsl(50, 10%, 10%)"); // [50, 10, 10]
```
