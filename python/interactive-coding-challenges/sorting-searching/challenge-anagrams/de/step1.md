# Anagramme

## Problem

Gegeben ein Array von Strings, schreiben Sie eine Funktion, um das Array zu sortieren, sodass alle Anagramme nebeneinander stehen. Ein Anagramm wird definiert als ein Wort oder eine Phrase, die durch Umordnung der Buchstaben eines anderen Wortes oder einer anderen Phrase gebildet wird. Beispielsweise sind "act" und "cat" Anagramme voneinander.

## Anforderungen

Um dieses Problem zu lösen, müssen die folgenden Anforderungen erfüllt werden:

- Die Funktion muss alle Anagramme im sortierten Array zusammen gruppieren.
- Es gibt keine anderen Sortieranforderungen außer der Gruppierung von Anagrammen.
- Die Eingaben können ungültig sein, daher muss die Funktion ungültige Eingaben verarbeiten.
- Die Funktion muss in den Arbeitsspeicher passen.

## Beispielverwendung

Die Funktion sollte in diesen Szenarien wie folgt verhalten:

- None -> Exception
- [] -> []
- Allgemeiner Fall
  - Eingabe: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
  - Ergebnis: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']
