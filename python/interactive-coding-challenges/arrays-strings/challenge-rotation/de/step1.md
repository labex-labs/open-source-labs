# Drehung

## Problemstellung

Gegeben zwei Strings s1 und s2, bestimmen Sie, ob s1 eine Drehung von s2 ist, indem Sie (nur einmal) eine Funktion is_substring aufrufen. Die Funktion is_substring nimmt zwei Strings als Eingabe und gibt True zurück, wenn der erste String ein Teilstring des zweiten Strings ist, und False sonst.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen erfüllen:

- Der String ist ASCII.
- Der Vergleich ist case-sensitive.
- Wir können zusätzliche Datenstrukturen verwenden.
- Die Strings passen in den Arbeitsspeicher.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie die Funktion verhalten sollte:

- Wenn die Strings unterschiedliche Größen haben, sollte die Funktion False zurückgeben.
- Wenn einer der Strings None ist, sollte die Funktion False zurückgeben.
- Wenn ein String ein Leerzeichen ist und der andere nicht, sollte die Funktion False zurückgeben.
- Wenn beide Strings Leerzeichen sind, sollte die Funktion True zurückgeben.
- Wenn s1 eine Drehung von s2 ist, sollte die Funktion True zurückgeben.
