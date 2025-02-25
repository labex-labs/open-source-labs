# Permutationen

## Problem

Gegeben einen Eingabestring, ist die Aufgabe, alle möglichen Permutationen der Zeichen im String zu finden. Die Ausgabe sollte eine Liste von Strings sein, wobei jeder String eine eindeutige Permutation des Eingabestrings darstellt. Der Eingabestring kann Duplikate enthalten, aber die Ausgabe darf keine Duplikate haben.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Der Input kann Duplikate enthalten.
- Die Ausgabe darf keine Duplikate haben.
- Die Ausgabe sollte eine Liste von Strings sein.
- Die Ergebnisse müssen nicht sortiert sein.
- Die Eingaben sind nicht immer gültig.
- Die Lösung sollte in den Arbeitsspeicher passen.

## Beispielverwendung

Hier sind einige Beispiele, wie die Funktion verhalten sollte:

- Wenn der Input None ist, sollte die Ausgabe None sein.
- Wenn der Input ein leerer String ist, sollte die Ausgabe ein leerer String sein.
- Wenn der Input 'AABC' ist, sollte die Ausgabe ['AABC', 'AACB', 'ABAC', 'ABCA', 'ACAB', 'ACBA', 'BAAC', 'BACA', 'BCAA', 'CAAB', 'CABA', 'CBAA'] sein.
