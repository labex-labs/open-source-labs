# Schleifenanfang finden

## Problemstellung

Gegeben ist eine singuläre verkettete Liste. Wir müssen den Anfang einer Schleife finden, sofern eine vorhanden ist. Eine Schleife wird definiert als ein Knoten in der Liste, der auf einen vorherigen Knoten zeigt und so einen Zyklus bildet. Wenn es keine Schleife gibt, geben wir None zurück. Wenn es eine Schleife gibt, geben wir den Knoten zurück, an dem die Schleife beginnt.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die verkettete Liste ist eine singuläre verkettete Liste.
- Wir dürfen nicht davon ausgehen, dass uns immer eine zirkuläre verkettete Liste übergeben wird.
- Wenn wir eine Schleife finden, geben wir den Knoten zurück, an dem die Schleife beginnt.
- Wir können davon ausgehen, dass wir bereits eine Klasse für verkettete Listen haben, die für dieses Problem verwendet werden kann.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie diese Funktion verwendet werden kann:

- Leere Liste -> None
- Nicht zirkuläre verkettete Liste -> None
  - Ein Element
  - Zwei oder mehr Elemente
- Allgemeiner Fall einer zirkulären verketteten Liste
