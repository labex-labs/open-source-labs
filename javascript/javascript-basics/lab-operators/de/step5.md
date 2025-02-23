# Nicht, Nicht-Gleich

Dies liefert den logisch entgegengesetzten Wert dessen, was ihm vorhergeht. Es verwandelt einen `true` in einen `false` usw. Wenn es zusammen mit dem Gleichheitsoperator verwendet wird, testet der Negationsoperator, ob zwei Werte nicht gleich sind.

Für "Nicht" ist der grundlegende Ausdruck wahr, aber der Vergleich liefert `false`, weil wir ihn negieren:

```js
// Not(!)
let myVariable = 3;
!(myVariable === 3);
```

"Nicht-Gleich" liefert im Grunde das gleiche Ergebnis mit unterschiedlicher Syntax. Hier testen wir, ob `myVariable` NICHT gleich 3 ist. Dies liefert `false`, weil `myVariable` gleich 3 ist:

```js
// Does-not-equal(!==)
let myVariable = 3;
myVariable !== 3;
```

Es gibt noch viele weitere Operatoren, die zu erkunden sind, aber das reicht für jetzt aus. Siehe [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators) für eine vollständige Liste.

> **Hinweis:** Beim Durchführen von Berechnungen kann das Mischen von Datentypen zu einigen seltsamen Ergebnissen führen. Achten Sie darauf, dass Sie Ihre Variablen korrekt referenzieren und die erwarteten Ergebnisse erhalten. Beispielsweise geben Sie `'35' + '25'` in Ihre Konsole ein. Warum erhalten Sie nicht das erwartete Ergebnis? Weil die Anführungszeichen die Zahlen zu Zeichenketten umwandeln, sodass Sie letztendlich Zeichenketten konkatenieren anstatt Zahlen zu addieren. Wenn Sie `35 + 25` eingeben, erhalten Sie die Summe der beiden Zahlen.
