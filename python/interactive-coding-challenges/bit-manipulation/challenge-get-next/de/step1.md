# Nächstes finden

## Problem

Gegeben eine positive ganze Zahl müssen Sie die nächstgrößere und die nächstkleinere Zahl mit der gleichen Anzahl von 1ern wie die gegebene Zahl finden. Beispielsweise, wenn die Eingabe 0000 0000 1101 0111 ist, sollte die Ausgabe für die nächstgrößere Zahl 0000 0000 1101 1011 und für die nächstkleinere Zahl 0000 0000 1100 1111 sein.

## Anforderungen

Um diese Aufgabe zu lösen, müssen Sie die folgenden Anforderungen erfüllen:

- Die Ausgabe sollte eine positive ganze Zahl sein.
- Die Eingaben können ungültig sein, daher müssen Sie Ausnahmen behandeln.
- Die Lösung sollte in den Arbeitsspeicher passen.

## Beispielverwendung

Hier sind einige Beispiele, wie diese Funktion verwendet werden kann:

- None -> Exception
- 0 -> Exception
- negative Ganzzahl -> Exception
- Allgemeiner Fall:

```txt
    * Eingabe:         0000 0000 1101 0111
    * Nächstgrößere:  0000 0000 1101 1011
    * Nächstkleinere: 0000 0000 1100 1111
```
