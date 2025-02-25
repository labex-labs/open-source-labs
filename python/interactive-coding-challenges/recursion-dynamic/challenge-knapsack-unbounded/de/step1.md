# Unbeschränktes Rucksackproblem

## Problemstellung

Gegeben ist ein Rucksack mit einer Gesamtgewichtskapazität und eine Liste von Gegenständen mit Gewicht w(i) und Wert v(i). Bestimmen Sie den maximalen Gesamtwert, den Sie tragen können. Die Gegenstände können beliebig oft ausgewählt werden.

## Anforderungen

Um das unbeschränkte Rucksackproblem zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- Die Gegenstände können ersetzt werden, nachdem sie im Rucksack platziert wurden.
- Ein Gegenstand kann nicht aufgeteilt werden.
- Die eingegebenen Gegenstände dürfen kein Gewicht oder Wert von 0 haben.
- Es muss nur der Gesamtwert zurückgegeben werden, nicht die Gegenstände, die den maximalen Gesamtwert ausmachen.
- Die Eingaben können ungültig sein, daher ist eine Validierung erforderlich.
- Die Eingaben sind nach Val/Wert sortiert.
- Speicherbeschränkungen sind kein Problem.

## Beispielverwendung

Das unbeschränkte Rucksackproblem kann in verschiedenen Szenarien eingesetzt werden, wie z. B. bei der Ressourcenallokation und der Optimierung von Finanzportfolios. Hier sind einige Beispiele für seine Verwendung:

- Wenn das Gesamtgewicht oder die Gegenstände None sind, sollte eine Ausnahme ausgelöst werden.
- Wenn das Gesamtgewicht oder die Gegenstände 0 sind, sollte das Ergebnis 0 sein.
- Für einen allgemeinen Fall nehmen wir an, dass das Gesamtgewicht 8 ist und die Gegenstände sind:

  | v   | w   |
  | --- | --- |
  | 0   | 0   |
  | 1   | 1   |
  | 3   | 2   |
  | 7   | 4   |

  Der maximale Wert, der getragen werden kann, ist 14.
