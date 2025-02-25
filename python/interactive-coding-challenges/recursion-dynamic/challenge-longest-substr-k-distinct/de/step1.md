# Längste Teilzeichenfolge mit k verschiedenen Zeichen

## Problemstellung

Gegeben einen String und eine ganze Zahl k, finde die Länge der längsten Teilzeichenfolge, die höchstens k verschiedene Zeichen enthält. Eine Teilzeichenfolge ist ein zusammenhängender Block von Zeichen. Beispielsweise ist in der Zeichenfolge "abcabcdefgghiij" die längste Teilzeichenfolge mit höchstens 3 verschiedenen Zeichen "abcabc". Wenn es mehrere Teilzeichenfolgen mit der gleichen Länge gibt, gebe beliebige von ihnen zurück.

## Anforderungen

Um diese Aufgabe zu lösen, müssen die folgenden Anforderungen erfüllt werden:

- Die Eingaben können ungültig sein, daher sollte der Code ungültige Eingaben优雅地 behandeln.
- Die Zeichenfolgen sind ASCII-Zeichenfolgen.
- Die Suche ist case-sensitive.
- Eine Teilzeichenfolge ist ein zusammenhängender Block von Zeichen.
- Das Ergebnis sollte eine ganze Zahl sein.
- Der Code sollte die Eingabe innerhalb der Speichergrenzen verarbeiten können.

## Beispielverwendung

Die folgenden Beispiele demonstrieren das erwartete Verhalten des Codes:

- None -> TypeError
- '', k = 3 -> 0
- 'abcabcdefgghiij', k=3 -> 6
- 'abcabcdefgghighij', k=3 -> 7
