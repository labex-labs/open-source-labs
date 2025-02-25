# Die längste aufsteigende Teilfolge

## Problemstellung

Gegeben ist eine Sequenz von ganzen Zahlen. Man soll die längste aufsteigende Teilfolge finden. Die Teilfolge kann nicht zusammenhängend sein und kann Duplikate enthalten. Wenn es mehrere Lösungen gibt, soll beliebig eine zurückgegeben werden.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Können Duplikate vorkommen?
  - Ja
- Können wir davon ausgehen, dass die Eingaben ganze Zahlen sind?
  - Ja
- Können wir davon ausgehen, dass die Eingaben gültig sind?
  - Nein, wir müssen ungültige Eingaben behandeln.
- Erwarten wir, dass das Ergebnis ein Array der längsten aufsteigenden Teilfolge ist?
  - Ja
- Können wir davon ausgehen, dass dies in den Speicher passt?
  - Ja

## Beispielverwendung

Hier sind einige Beispiele, wie diese Funktion verwendet werden kann:

- Keine Eingabe -> Exception
- [] -> []
- [3, 4, -1, 0, 6, 2, 3] -> [-1, 0, 2, 3]
