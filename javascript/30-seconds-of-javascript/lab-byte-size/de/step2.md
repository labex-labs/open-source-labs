# Die Verwendung von Blob zur Berechnung der Byte-Größe von Zeichenketten

Nachdem wir nun die Zeichenkettenrepräsentation verstehen, lernen wir, wie man die tatsächliche Byte-Größe einer Zeichenkette mithilfe des `Blob`-Objekts berechnet.

Ein `Blob` (Binary Large Object) repräsentiert ein dateiähnliches Objekt aus unveränderlichen, Rohdaten. Indem wir unsere Zeichenkette in einen Blob umwandeln, können wir auf seine `size`-Eigenschaft zugreifen, um die Byte-Größe zu bestimmen.

In der Node.js-Konsole erstellen wir eine Funktion zur Berechnung der Byte-Größe:

```javascript
const byteSize = (str) => new Blob([str]).size;
```

Diese Funktion nimmt eine Zeichenkette als Eingabe, wandelt sie in einen Blob um und gibt seine Größe in Bytes zurück.

Testen wir diese Funktion an einem einfachen Beispiel:

```javascript
byteSize("Hello World");
```

Sie sollten die folgende Ausgabe sehen:

```
11
```

In diesem Fall sind die Anzahl der Zeichen und die Byte-Größe gleich, da "Hello World" nur ASCII-Zeichen enthält, die jeweils durch ein einzelnes Byte repräsentiert werden.

Versuchen wir es nun mit einem Nicht-ASCII-Zeichen:

```javascript
byteSize("😀");
```

Sie sollten die folgende Ausgabe sehen:

```
4
```

Dies zeigt, dass das Emoji zwar als einzelnes Zeichen erscheint, aber tatsächlich 4 Bytes Speicherplatz beansprucht.
