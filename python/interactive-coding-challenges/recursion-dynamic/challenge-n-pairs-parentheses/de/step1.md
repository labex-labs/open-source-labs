# n Klammerpaare

## Problem

Das Problem besteht darin, alle gültigen Kombinationen von n Klammerpaaren zu finden. Eine gültige Kombination ist eine, in der jede öffnende Klammer eine entsprechende schließende Klammer hat und die Klammerpaare richtig geschachtelt sind. Beispielsweise sind die folgenden gültige Kombinationen von 3 Klammerpaaren:

- ((()))
- (()())
- (())()
- ()(())
- ()()()

Die folgenden sind keine gültigen Kombinationen von 3 Klammerpaaren:

- )()(
- ((()
- ))((
- ()()()

## Anforderungen

Um dieses Problem zu lösen, müssen wir auf folgende Fragen antworten:

- Ist die Eingabe eine Ganzzahl, die die Anzahl der Paare repräsentiert?
  - Ja, die Eingabe ist eine Ganzzahl, die die Anzahl der Paare repräsentiert.
- Können wir annehmen, dass die Eingaben gültig sind?
  - Nein, wir können nicht annehmen, dass die Eingaben gültig sind.
- Ist die Ausgabe eine Liste von gültigen Kombinationen?
  - Ja, die Ausgabe ist eine Liste von gültigen Kombinationen.
- Soll die Ausgabe Duplikate enthalten?
  - Nein, die Ausgabe sollte keine Duplikate enthalten.
- Können wir annehmen, dass dies im Speicher passt?
  - Ja, wir können annehmen, dass dies im Speicher passt.

## Beispielverwendung

Die folgenden sind Beispielverwendungen der Funktion:

- None -> Exception
- Negative -> Exception
- 0 -> []
- 1 -> ['()']
- 2 -> ['(())', '()()']
- 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
