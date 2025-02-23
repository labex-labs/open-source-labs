# Umwandeln eines Arrays in ein Flags-Objekt

Wenn Sie beginnen möchten, zu programmieren, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Die folgende Funktion wandelt ein Array von Strings in ein Objekt um, das auf `true` abbildet.

Dazu verwenden wir `Array.prototype.reduce()`. Diese Methode wandelt das Array in ein Objekt um, wobei jeder Array-Wert als Schlüssel fungiert, dessen Wert auf `true` gesetzt wird.

```js
const flags = (arr) => arr.reduce((acc, str) => ({ ...acc, [str]: true }), {});
```

Hier ist ein Beispiel:

```js
flags(["red", "green"]); // { red: true, green: true }
```
