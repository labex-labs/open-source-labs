# Längste Teilzeichenfolge

## Problemstellung

Gegeben zwei Zeichenketten soll die längste gemeinsame Teilzeichenfolge gefunden werden. Eine Teilzeichenfolge ist ein zusammenhängender Block von Zeichen. Die Lösung sollte case-sensitive sein und davon ausgehen, dass die Zeichenketten ASCII-Zeichen sind. Die Ausgabe sollte eine Zeichenkette sein und das Programm sollte davon ausgehen, dass die Eingaben nicht unbedingt gültig sind. Es kann jedoch davon ausgehen, dass das Problem in den Arbeitsspeicher passt.

## Anforderungen

Um dieses Problem zu lösen, muss das Programm die folgenden Anforderungen erfüllen:

- Die Eingaben sind nicht unbedingt gültig.
- Die Zeichenketten sind ASCII-Zeichen.
- Die Lösung sollte case-sensitive sein.
- Eine Teilzeichenfolge ist ein zusammenhängender Block von Zeichen.
- Die Ausgabe sollte eine Zeichenkette sein.
- Das Programm sollte davon ausgehen, dass das Problem in den Arbeitsspeicher passt.

## Beispielverwendung

Das Programm sollte sich wie folgt verhalten:

- Wenn str0 oder str1 None ist, sollte eine Ausnahme ausgelöst werden.
- Wenn str0 oder str1 gleich 0 ist, sollte die Ausgabe eine leere Zeichenkette sein.
- Im Allgemeinen, gegeben str0 = 'ABCDEFGHIJ' und str1 = 'FOOBCDBCDE', sollte die Ausgabe 'BCDE' sein.
