# Wie man die Byte-Größe einer Zeichenkette in JavaScript erhält

Um die Byte-Größe einer Zeichenkette in JavaScript zu erhalten, befolgen Sie diese Schritte:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
2. Konvertieren Sie die Zeichenkette in ein [`Blob`-Objekt](https://developer.mozilla.org/en-US/docs/Web/API/Blob).
3. Verwenden Sie `Blob.size`, um die Länge der Zeichenkette in Bytes zu erhalten.

Hier ist der JavaScript-Code, um die Byte-Größe einer Zeichenkette zu erhalten:

```js
const byteSize = (str) => new Blob([str]).size;
```

Sie können diese Funktion mit den folgenden Beispielen testen:

```js
byteSize("😀"); // 4
byteSize("Hello World"); // 11
```
