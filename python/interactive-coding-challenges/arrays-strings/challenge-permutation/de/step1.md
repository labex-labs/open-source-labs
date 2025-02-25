# Permutation

## Problem

Gegeben zwei Strings müssen wir bestimmen, ob ein String eine Permutation des anderen ist. Eine Permutation wird als eine Umordnung der Zeichen in einem String definiert. Beispielsweise ist "act" eine Permutation von "cat".

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Der String ist ASCII.
- Leerzeichen sind wichtig.
- Der Vergleich ist case-sensitive. Beispielsweise stimmen "Nib" und "bin" nicht überein.
- Wir können zusätzliche Datenstrukturen verwenden.
- Wir können davon ausgehen, dass die Strings in den Arbeitsspeicher passen.

## Beispielverwendung

Hier sind einige Beispiele, wie diese Funktion verwendet werden kann:

- Ein oder mehrere None-Eingaben -> False
- Ein oder mehrere leere Strings -> False
- 'Nib', 'bin' -> False
- 'act', 'cat' -> True
- 'a ct', 'ca t' -> True
