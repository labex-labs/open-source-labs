# Ein Zeichenkette in JavaScript abkürzen

Um eine Zeichenkette in JavaScript abzukürzen, können Sie die `truncateString`-Funktion verwenden. Diese Funktion nimmt zwei Argumente entgegen: `str` (die zu abkürzende Zeichenkette) und `num` (die maximale Länge der abgekürzten Zeichenkette).

Die `truncateString`-Funktion überprüft, ob die Länge von `str` größer als `num` ist. Wenn ja, kürzt die Funktion die Zeichenkette auf die gewünschte Länge und fügt `'...'` am Ende hinzu. Wenn nicht, gibt sie die ursprüngliche Zeichenkette zurück.

Hier ist der Code für die `truncateString`-Funktion:

```js
const truncateString = (str, num) =>
  str.length > num ? str.slice(0, num > 3 ? num - 3 : num) + "..." : str;
```

Und hier ist ein Beispiel dafür, wie die `truncateString`-Funktion verwendet werden kann:

```js
truncateString("boomerang", 7); // 'boom...'
```
