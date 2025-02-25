# Potenzmenge

## Problemstellung

Gegeben eine Menge, geben Sie alle möglichen Teilmengen der Menge zurück. Die Teilmengen sollten eindeutig sein, was bedeutet, dass zwei Teilmengen, die die gleichen Elemente haben, als die gleiche Teilmenge behandelt werden sollten. Die leere Menge sollte ebenfalls als Teilmenge enthalten sein. Die Eingaben sind nicht notwendigerweise eindeutig, und wir können nicht davon ausgehen, dass die Eingaben gültig sind. Wir können jedoch davon ausgehen, dass das Problem in den Arbeitsspeicher passt.

## Anforderungen

Um die Potenzmenge einer Menge zu generieren, müssen wir die folgenden Anforderungen erfüllen:

- Die resultierenden Teilmengen sollten eindeutig sein und Teilmengen mit denselben Elementen als gleich behandeln.
- Die leere Menge sollte als Teilmenge enthalten sein.
- Die Eingaben sind nicht notwendigerweise eindeutig.
- Wir können nicht davon ausgehen, dass die Eingaben gültig sind.
- Wir können davon ausgehen, dass das Problem in den Arbeitsspeicher passt.

## Beispielverwendung

```txt
* None -> None
* [] -> [[]]
* ['a'] -> [[],
            ['a']]
* ['a', 'b'] -> [[],
                 ['a'],
                 ['b'],
                 ['a', 'b']]
* ['a', 'b', 'c'] -> [[],
                      ['a'],
                      ['b'],
                      ['c'],
                      ['a', 'b'],
                      ['a', 'c'],
                      ['b', 'c'],
                      ['a', 'b', 'c']]
```
