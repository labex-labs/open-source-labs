# Testen mit verschiedenen Zeichenkettenarten

Lassen Sie uns untersuchen, wie verschiedene Zeichentypen die Byte-Größe einer Zeichenkette beeinflussen.

In der Node.js-Konsole testen wir unsere `byteSize`-Funktion mit verschiedenen Zeichenketten:

1. Einfacher englischer Text:

```javascript
byteSize("The quick brown fox jumps over the lazy dog");
```

Erwartete Ausgabe:

```
43
```

2. Zahlen und Sonderzeichen:

```javascript
byteSize("123!@#$%^&*()");
```

Erwartete Ausgabe:

```
13
```

3. Eine Mischung aus ASCII- und Nicht-ASCII-Zeichen:

```javascript
byteSize("Hello, 世界!");
```

Erwartete Ausgabe:

```
13
```

4. Mehrere Emojis:

```javascript
byteSize("😀😃😄😁");
```

Erwartete Ausgabe:

```
16
```

Beachten Sie, dass bei gemischten Zeichentypen, insbesondere bei Nicht-ASCII-Zeichen wie chinesischen Zeichen und Emojis, die Byte-Größe größer ist als die Anzahl der Zeichen.

Dies ist wichtig zu verstehen, wenn Sie mit Daten arbeiten, die möglicherweise internationale Zeichen oder Sonderzeichen enthalten, da dies die Speicheranforderungen und die Datenübertragungsgrößen beeinflusst.

Lassen Sie uns die Node.js-Konsole verlassen, indem wir Folgendes eingeben:

```javascript
.exit
```

Dadurch gelangen Sie zurück zum normalen Terminal-Prompt.
