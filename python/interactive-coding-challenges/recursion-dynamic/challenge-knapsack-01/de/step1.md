# 0/1-Rucksackproblem

## Problemstellung

Gegeben ist ein Rucksack mit einer Gesamtgewichtskapazität und eine Liste von Gegenständen mit Gewicht w(i) und Wert v(i). Bestimmen Sie, welche Gegenstände ausgewählt werden sollen, um den Gesamtwert zu maximieren. Das Problem ist als 0/1-Rucksackproblem bekannt, da jeder Gegenstand nur einmal ausgewählt werden kann (0/1 Entscheidung). Das Problem ist NP-schwer, was bedeutet, dass es kein bekanntes polynomielles Zeitalgorithmus gibt, der es in allen Fällen optimal lösen kann.

## Anforderungen

Um das Rucksackproblem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die Gegenstände können nicht ersetzt werden, nachdem sie im Rucksack platziert wurden.
- Wir können keinen Gegenstand aufteilen.
- Wir können keinen Eingabegegenstand mit Gewicht oder Wert 0 haben.
- Wir dürfen nicht annehmen, dass die Eingaben gültig sind.
- Die Eingaben sollten nach Val/Gewicht sortiert sein.
- Wir können annehmen, dass das Problem in den Arbeitsspeicher passt.

## Beispiel

Hier ist ein Beispiel, wie das Rucksack-Algorithmus verwendet werden kann:

```txt
Gesamtgewicht = 8
Gegenstände
  v | w
  0 | 0
a 2 | 2
b 4 | 2
c 6 | 4
d 9 | 5

Maximalwert = 13
Gegenstände
  v | w
b 4 | 2
d 9 | 5
```

In diesem Beispiel haben wir einen Rucksack mit einer Gesamtgewichtskapazität von 8 und vier Gegenstände mit ihren jeweiligen Werten und Gewichten. Wir müssen die Gegenstände auswählen, die den Gesamtwert maximieren, während das Gewicht innerhalb der Kapazität des Rucksacks bleibt. Die optimale Lösung ist, die Gegenstände b und d auszuwählen, die einen Gesamtwert von 13 und ein Gesamtgewicht von 7 haben.
