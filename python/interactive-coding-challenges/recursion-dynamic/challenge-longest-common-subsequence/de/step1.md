# Längste gemeinsame Teilfolge

## Problemstellung

Gegeben zwei Strings, finde die längste gemeinsame Teilfolge. Eine Teilfolge ist eine Folge, die aus einer anderen Folge durch Löschen einiger oder keiner Elemente ohne Änderung der Reihenfolge der verbleibenden Elemente abgeleitet werden kann. Beispielsweise ist "ACE" eine Teilfolge von "ABCDE", aber nicht von "AEDCA".

## Anforderungen

Um dieses Problem zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- Die Eingaben können ungültig sein, daher sollte das Programm ungültige Eingaben verarbeiten.
- Die Strings sind ASCII-codiert.
- Das Programm sollte case-sensitive sein.
- Eine Teilfolge ist ein nicht zusammenhängender Block von Zeichen.
- Das Programm sollte einen String als Ergebnis zurückgeben.
- Das Programm sollte davon ausgehen, dass es in den verfügbaren Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie das Programm verhalten sollte:

- Wenn str0 oder str1 None ist, sollte eine Ausnahme ausgelöst werden.
- Wenn str0 oder str1 gleich 0 ist, sollte ein leerer String zurückgegeben werden.
- Allgemeiner Fall:

```
str0 = 'ABCDEFGHIJ'
str1 = 'FOOBCDBCDE'

Ergebnis: 'BCDE'
```
