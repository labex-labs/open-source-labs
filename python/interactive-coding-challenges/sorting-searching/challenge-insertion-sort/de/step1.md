# EinfügeSortieralgorithmus

## Problem

Das Problem besteht darin, den EinfügeSortieralgorithmus in Python zu implementieren. Gegeben eine unsortierte Liste von Elementen soll der Algorithmus die Liste aufsteigend sortieren. Der Algorithmus funktioniert, indem er über die Liste iteriert und jedes Element an seiner richtigen Position in dem sortierten Teil der Liste einfügt.

Der Algorithmus beginnt damit, dass er annimmt, dass das erste Element in der Liste bereits sortiert ist. Anschließend iteriert er über die verbleibenden Elemente in der Liste und vergleicht jedes Element mit den Elementen im sortierten Teil der Liste. Wenn das Element kleiner als das aktuelle Element im sortierten Teil der Liste ist, wird es vor diesem Element eingefügt. Wenn das Element größer als alle Elemente im sortierten Teil der Liste ist, wird es am Ende des sortierten Teils der Liste eingefügt.

## Anforderungen

Um den EinfügeSortieralgorithmus in Python zu implementieren, sollten die folgenden Anforderungen erfüllt werden:

- Eine naive Lösung ist ausreichend.
- Duplikate sind erlaubt.
- Die Eingabe ist nicht notwendigerweise gültig, daher sollte der Algorithmus ungültige Eingaben优雅 behandeln.
- Der Algorithmus sollte in den Arbeitsspeicher passen.

## Beispielverwendung

Die folgenden sind einige Beispiele, wie der EinfügeSortieralgorithmus verwendet werden kann:

- None -> Exception: Wenn die Eingabe None ist, sollte eine Exception ausgelöst werden.
- Leere Eingabe -> []: Wenn die Eingabe eine leere Liste ist, sollte die Ausgabe ebenfalls eine leere Liste sein.
- Ein Element -> [element]: Wenn die Eingabe eine Liste mit nur einem Element ist, sollte die Ausgabe die gleiche Liste sein.
- Zwei oder mehr Elemente: Wenn die Eingabe eine Liste mit zwei oder mehr Elementen ist, sollte die Ausgabe eine aufsteigend sortierte Liste sein.
