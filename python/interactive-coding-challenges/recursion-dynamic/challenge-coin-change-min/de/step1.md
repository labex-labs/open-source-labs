# Münzwechsel - Minimale Anzahl

## Problemstellung

Gegeben eine Menge von Münzen mit Denominationen kleiner als n Cent, müssen wir die minimale Anzahl von Möglichkeiten bestimmen, um n Cent mit diesen Münzen zu bilden. Die Münzen können in beliebiger Kombination verwendet werden, und wir haben eine unbegrenzte Anzahl von Münzen jeder Denomination. Wir müssen nicht die Kombination(en) der Münzen angeben, die die minimale Anzahl darstellen.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die Münzen müssen genau n Cent erreichen.
- Wir können annehmen, dass wir eine unbegrenzte Anzahl von Münzen haben, um n Cent zu bilden.
- Wir müssen nicht die Kombination(en) der Münzen angeben, die die minimale Anzahl darstellen.
- Wir dürfen nicht annehmen, dass die Münzdenominationen in aufsteigender Reihenfolge gegeben sind.
- Wir können annehmen, dass dies in den verfügbaren Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele, wie diese Funktion verwendet werden kann:

- Münzen: None oder n: None -> Exception
- Münzen: [] oder n: 0 -> 0
- Münzen: [1, 2, 3] oder [3, 2, 1] -> 2
